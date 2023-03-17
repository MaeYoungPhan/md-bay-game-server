import json
from rest_framework import status
from rest_framework.test import APITestCase
from baygameapi.models import RecordOfTrip, Occasion, Gamer
from rest_framework.authtoken.models import Token


class TripTests(APITestCase):

    fixtures = ['users', 'tokens', 'gamers', 'occasions', 'record_of_trips']

    def setUp(self):
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_trip(self):
        """
        Ensure we can create a new trip.
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/recordoftrips"

        # Define the request body
        data = {
            "date": "2022-07-11",
            "name": "Sailing",
            "occasion": 11,
            "number_found": 15,
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["date"], "2022-07-11")
        self.assertEqual(json_response["name"], "Sailing")
        self.assertEqual(json_response["number_found"], 15)

    def test_get_trip(self):
        """
        Ensure we can get an existing trip.
        """

        # Seed the database with a trip
        trip = RecordOfTrip()
        trip.date = "2023-05-31"
        trip.name = "Memorial Day"
        trip.gamer_id = 1
        trip.occasion_id = 2
        trip.number_found = 4
        trip.save()

        # Initiate request and store response
        response = self.client.get(f"/recordoftrips/{trip.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["date"], "2023-05-31")
        self.assertEqual(json_response["name"], "Memorial Day")
        self.assertEqual(json_response["number_found"], 4)

    def test_change_trip(self):
        """
        Ensure we can change an existing trip.
        """
        trip = RecordOfTrip()
        trip.date = "2023-05-31"
        trip.name = "Memorial Day"
        trip.gamer_id = 1
        trip.occasion_id = 2
        trip.number_found = 4
        trip.save()

        # DEFINE NEW PROPERTIES FOR TRIP
        data = {
            "date": "2023-05-26",
            "name": "Memorial Day",
            "occasion": 1,
            "number_found": 14
        }

        response = self.client.put(f"/recordoftrips/{trip.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET trip again to verify changes were made
        response = self.client.get(f"/recordoftrips/{trip.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["date"], "2023-05-26")
        self.assertEqual(json_response["name"], "Memorial Day")
        self.assertEqual(json_response["number_found"], 14)

    def test_delete_trip(self):
        """
        Ensure we can delete an existing trip.
        """
        trip = RecordOfTrip()
        trip.date = "2023-05-31"
        trip.name = "Memorial Day"
        trip.gamer_id = 1
        trip.occasion_id = 2
        trip.number_found = 4
        trip.save()

        # DELETE the game you just created
        response = self.client.delete(f"/recordoftrips/{trip.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the game again to verify you get a 404 response
        response = self.client.get(f"/recordoftrips/{trip.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
