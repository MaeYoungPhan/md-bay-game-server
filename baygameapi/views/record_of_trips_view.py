"""View module for handling requests about game"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from baygameapi.models import RecordOfTrip, Gamer, Occasion


class RecordOfTripView(ViewSet):
    """Bay Game record of trips view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip
        Returns:
            Response -- JSON serialized trip
        """

        current_user = Gamer.objects.get(user=request.auth.user)

        try:
            trip = RecordOfTrip.objects.get(pk=pk) #make connection with server to return single query set where the primary key matches the pk requested by the client and assigns the object instance found to the trip variable
            
            if trip.gamer == current_user:
                trip.author = True
        
        except RecordOfTrip.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        serializer = TripSerializer(trip) #passes the instance stored in game through serializer to become a JSON stringified object and assigns it to serializer variable

        return Response(serializer.data, status=status.HTTP_200_OK) # returns serializer data to the client as a response. Response body is JSON stringified object of requested data.

    def list(self, request):
        """Handle GET requests to get all records of trips
        Returns:
            Response -- JSON serialized list of records of trips
        """
        # Make connection with server to retrieve a query set of all game items requested by client and assign the found instances to the game variable
        trips = RecordOfTrip.objects.all()
        #passes instances stored in trip variable to the serializer class to construct data into JSON stringified objects, which it then assigns to variable serializer
        current_user = Gamer.objects.get(user=request.auth.user)

        gamer_id = current_user.user_id

        if gamer_id is not None:
            
            record_of_trips = trips.filter(gamer_id=gamer_id)
        
        serializer = TripSerializer(record_of_trips, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK) #Constructs response and returns data requested by the client in the response body as an array of JSON stringified objects

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """
        gamer_id = Gamer.objects.get(user=request.auth.user) # connect with database and get user object based on token
        occasion = Occasion.objects.get(pk=request.data["occasion"]) # connect with database to retrieve occasion object

        trip = RecordOfTrip.objects.create(
            gamer=gamer_id,
            date=request.data["date"],
            name=request.data["name"],
            occasion=occasion,
            number_found=request.data["number_found"]
        )
        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a trip
        Returns:
            Response -- Empty body with 204 status code
        """

        trip = RecordOfTrip.objects.get(pk=pk)
        trip.date = request.data["date"]
        trip.name = request.data["name"]
        trip.number_found = request.data["number_found"]

        occasion = Occasion.objects.get(pk=request.data["occasion"])
        trip.occasion = occasion
        trip.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        trip = RecordOfTrip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GamerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gamer
        fields = ('id', 'user')

class OccasionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Occasion
        fields = ('id', 'name', 'emoji')


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for records of trips"""
    # Converts meta data requested to JSON stringified object using RecordOfTrip as model
    gamer = GamerSerializer(many=False)
    occasion = OccasionSerializer(many=False)
    class Meta: # configuration for serializer
        model = RecordOfTrip # model to use
        fields = ('id', 'gamer', 'date', 'name',  'occasion', 'number_found', 'author') # fields to include