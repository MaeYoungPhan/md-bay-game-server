"""View module for handling requests about event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from baygameapi.models import BayItem, Gamer
from rest_framework.decorators import action


class BayItemView(ViewSet):
    """Bay Game Bay Item view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single bay_item
        Returns:
            Response -- JSON serialized bay_item
        """
        try:
            bay_item = BayItem.objects.get(pk=pk) #make connection with server to return single query set where the primary key matches the pk requested by the client and assigns the object instance found to the event variable

            serializer = BayItemSerializer(bay_item) #passes the instance stored in event through serializer to become a JSON stringified object and assigns it to serializer variable

            return Response(serializer.data, status=status.HTTP_200_OK) # returns serializer data to the client as a response. Response body is JSON stringified object of requested data.

        except BayItem.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all bay items
        Returns:
            Response -- JSON serialized list of bay items
        """
        # Make connection with server to retrieve a query set of all bay items requested by client and assign the found instances to the bay_items variable
        bay_items = BayItem.objects.all()

        # Set the `found` property on every bay item
        for bay_item in bay_items:
            gamer = Gamer.objects.get(user=request.auth.user)
            # Check to see if the gamer has marked the items as found
            bay_item.found = gamer in bay_item.gamers.all()

        #passes instances stored in event variable to the serializer class to construct data into JSON stringified objects, which it then assigns to variable serializer
        serializer = BayItemSerializer(bay_items, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) #Constructs response and returns data requested by the client in the response body as an array of JSON stringified objects

    @action(methods=['post'], detail=True)
    def find(self, request, pk):
        """Post request for a user to sign up for an event"""

        gamer = Gamer.objects.get(user=request.auth.user)
        bay_item = BayItem.objects.get(pk=pk)
        bay_item.gamers.add(gamer)
        return Response({'message': 'Item found'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def reset(self, request, pk):
        """Delete request for a user to un-sign up for an event"""

        gamer = Gamer.objects.get(user=request.auth.user)
        bay_item = BayItem.objects.get(pk=pk)
        bay_item.gamers.remove(gamer)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BayItemSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    # Converts meta data requested to JSON stringified object using BayItem as model

    class Meta: # configuration for serializer
        model = BayItem # model to use
        fields = ('id', 'name', 'default_img', 'found_img', 'gamers', 'found') # fields to include
