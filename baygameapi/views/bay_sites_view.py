"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from baygameapi.models import BaySite, SiteSticker


class BaySiteView(ViewSet):
    """Bay Game Bay Sites view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single site
        Returns:
            Response -- JSON serialized site
        """
        try:
            site = BaySite.objects.get(pk=pk) #make connection with server to return single query set where the primary key matches the pk requested by the client and assigns the object instance found to the site variable

        except BaySite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BaySiteSerializer(site) #passes the instance stored in water through serializer to become a JSON stringified object and assigns it to serializer variable

        return Response(serializer.data, status=status.HTTP_200_OK) # returns serializer data to the client as a response. Response body is JSON stringified object of requested data.


    def list(self, request):
        """Handle GET requests to get all bay sites
        Returns:
            Response -- JSON serialized list of bay sites
        """
        # Make connection with server to retrieve a query set of all bay sites requested by client and assign the found instances to the sites variable
        sites = BaySite.objects.all()
        #passes instances stored in sites variable to the serializer class to construct data into JSON stringified objects, which it then assigns to variable serializer
        serializer = BaySiteSerializer(sites, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) #Constructs response and returns data requested by the client in the response body as an array of JSON stringified objects

class BaySiteSerializer(serializers.ModelSerializer):
    """JSON serializer for bay sites"""
    # Converts meta data requested to JSON stringified object using BaySite as model
    class Meta: # configuration for serializer
        model = BaySite # model to use
        fields = ('id', 'name', 'miles_to_oc', 'image', 'content', 'latitude', 'longitude') # fields to include
