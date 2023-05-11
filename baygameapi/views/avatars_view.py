"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from baygameapi.models import Avatar


class AvatarView(ViewSet):
    """Bay Game Avatars view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single avatar
        Returns:
            Response -- JSON serialized avatar
        """
        try:
            avatar = Avatar.objects.get(pk=pk) #make connection with server to return single query set where the primary key matches the pk requested by the client and assigns the object instance found to the game_type variable

        except Avatar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AvatarSerializer(avatar) #passes the instance stored in avatar through serializer to become a JSON stringified object and assigns it to serializer variable

        return Response(serializer.data, status=status.HTTP_200_OK) # returns serializer data to the client as a response. Response body is JSON stringified object of requested data.


    def list(self, request):
        """Handle GET requests to get all avatars
        Returns:
            Response -- JSON serialized list of avatars
        """
        # Make connection with server to retrieve a query set of all avatars items requested by client and assign the found instances to the game_types variable
        avatar = Avatar.objects.all()
        #passes instances stored in avatar variable to the serializer class to construct data into JSON stringified objects, which it then assigns to variable serializer
        serializer = AvatarSerializer(avatar, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) #Constructs response and returns data requested by the client in the response body as an array of JSON stringified objects

class AvatarSerializer(serializers.ModelSerializer):
    """JSON serializer for rivers and streams"""
    # Converts meta data requested to JSON stringified object using Avatar as model
    class Meta: # configuration for serializer
        model = Avatar # model to use
        fields = ('id', 'name', 'image') # fields to include
