import json
from rest_framework import status
from rest_framework.test import APITestCase
from baygameapi.models import BayItem, Gamer
from rest_framework.authtoken.models import Token


class BayItemsTests(APITestCase):

    fixtures = ['users', 'tokens', 'gamers', 'bay_items']

    def setUp(self):
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_bay_item(self):
        """
        Ensure we can get an existing bay item.
        """

        bay_item = BayItem()
        bay_item.name = "Ol' Blue"
        bay_item.default_img = "https://res.cloudinary.com/dungnytvx/image/upload/v1678979247/OlBlue_hk0nzi.png"
        bay_item.found_img = "https://res.cloudinary.com/dungnytvx/image/upload/v1678979247/OlBlue_hk0nzi.png"
        bay_item.save()

        response = self.client.get(f"/bayitems/{bay_item.id}")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response["name"], "Ol' Blue")
        self.assertEqual(json_response["default_img"], "https://res.cloudinary.com/dungnytvx/image/upload/v1678979247/OlBlue_hk0nzi.png")
        self.assertEqual(json_response["found_img"], "https://res.cloudinary.com/dungnytvx/image/upload/v1678979247/OlBlue_hk0nzi.png")

    def test_find_reset_bay_item(self):
        """
        Ensure we can find/reset a bay_item by adding/removing from found_items table using find and reset custom actions.
        """

        bay_item = BayItem()
        bay_item.name = "Ol' Blue"
        bay_item.default_img = "https://res.cloudinary.com/dungnytvx/image/upload/v1678979247/OlBlue_hk0nzi.png"
        bay_item.found_img = "https://res.cloudinary.com/dungnytvx/image/upload/v1678979247/OlBlue_hk0nzi.png"
        bay_item.save()

        gamer = 1

        bay_item.gamers.add(gamer)

        response = self.client.post(f"/bayitems/{bay_item.id}/find")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["message"],"Item found")

        response = self.client.delete(f"/bayitems/{bay_item.id}/reset")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)