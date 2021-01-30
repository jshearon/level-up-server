import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType, Game, Gamer, Event


class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "jon",
            "password": "Admin8*",
            "email": "jon@gmail.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Jon",
            "last_name": "Shearon",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        gametype = GameType()
        gametype.label = "Board game"
        gametype.save()

        game = Game()
        game.gametype = GameType.objects.get(pk=1)
        game.skill_level = 5
        game.title = "Clue"
        game.maker = "Milton Bradley"
        game.number_of_players = 6
        game.gamer = Gamer.objects.get(pk=1)
        game.save()

    def test_create_event(self):
        """
        Ensure we can create a new game.
        """
        # DEFINE GAME PROPERTIES
        url = "/events"
        data = {
            "time": "12:30:00",
            "date": "2021-02-14",
            "description": "New Event",
            "gameId": 1,
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["description"], "New Event")
        self.assertEqual(json_response["date"], "2021-02-14")
        self.assertEqual(json_response["time"], "12:30:00")

    def test_get_event(self):
        """
        Ensure we can get an existing game.
        """

        # Seed the database with a game
        event = Event()
        event.description = "Test"
        event.date = "2021-02-14"
        event.time = "12:30:00"
        event.organizer = Gamer.objects.get(pk=1)
        event.game = Game.objects.get(pk=1)

        event.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/events/{event.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["description"], "Test")
        self.assertEqual(json_response["date"], "2021-02-14")
        self.assertEqual(json_response["time"], "12:30:00")
        self.assertEqual(json_response["organizer"]["id"], 1)
        self.assertEqual(json_response["game"]["id"], 1)
