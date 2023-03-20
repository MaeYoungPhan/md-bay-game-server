import json
from rest_framework import status
from rest_framework.test import APITestCase
from baygameapi.models import Gamer, Occasion
from rest_framework.authtoken.models import Token


class OccasionsTests(APITestCase):

    fixtures = ['users', 'tokens', 'gamers', 'occasions']

    def setUp(self):
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_occasion(self):
        """
        Ensure we can get an existing occasion.
        """

        occasion = Occasion()
        occasion.name = "Goat Herding"
        occasion.emoji = "🐐"
        occasion.save()

        response = self.client.get(f"/occasions/{occasion.id}")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response["name"], "Goat Herding")
        self.assertEqual(json_response["emoji"], "🐐")