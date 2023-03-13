"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from baygameapi.models import RiverAndStream


class RiverAndStreamView(ViewSet):
    """Bay Game River and Streams view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single river or stream
        Returns:
            Response -- JSON serialized river or stream
        """
        try:
            water = RiverAndStream.objects.get(pk=pk) #make connection with server to return single query set where the primary key matches the pk requested by the client and assigns the object instance found to the game_type variable

        except RiverAndStream.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RiverAndStreamSerializer(water) #passes the instance stored in water through serializer to become a JSON stringified object and assigns it to serializer variable

        return Response(serializer.data, status=status.HTTP_200_OK) # returns serializer data to the client as a response. Response body is JSON stringified object of requested data.


    def list(self, request):
        """Handle GET requests to get all rivers and streams
        Returns:
            Response -- JSON serialized list of rivers and streams
        """
        # Make connection with server to retrieve a query set of all rivers and streams items requested by client and assign the found instances to the game_types variable
        water = RiverAndStream.objects.all()
        #passes instances stored in water variable to the serializer class to construct data into JSON stringified objects, which it then assigns to variable serializer
        serializer = RiverAndStreamSerializer(water, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) #Constructs response and returns data requested by the client in the response body as an array of JSON stringified objects

class RiverAndStreamSerializer(serializers.ModelSerializer):
    """JSON serializer for rivers and streams"""
    # Converts meta data requested to JSON stringified object using RiverAndStream as model
    class Meta: # configuration for serializer
        model = RiverAndStream # model to use
        fields = ('id', 'name', 'miles_to_bay') # fields to include
