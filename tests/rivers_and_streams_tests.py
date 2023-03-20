import json
from rest_framework import status
from rest_framework.test import APITestCase
from baygameapi.models import Gamer, RiverAndStream
from rest_framework.authtoken.models import Token


class RiverStreamsTests(APITestCase):

    fixtures = ['users', 'tokens', 'gamers', 'river_and_streams']

    def setUp(self):
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_river(self):
        """
        Ensure we can get an existing river or stream.
        """

        riverandstream = RiverAndStream()
        riverandstream.name = "Tennessee"
        riverandstream.miles_to_bay = "544.00"
        riverandstream.save()

        response = self.client.get(f"/riverandstreams/{riverandstream.id}")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response["name"], "Tennessee")
        self.assertEqual(json_response["miles_to_bay"], "544.00")
