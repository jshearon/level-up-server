"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Game, GameType, Event
from levelupreports.views import Connection


def userevent_list(request):
    """Function to build an HTML report of games by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            db_cursor.execute("""
                SELECT
                    u.id as user_id,
                    u.first_name || ' ' || u.last_name AS full_name,
                    e.id,
                    e.description,
                    e.date,
                    e.time,
                    g.id as game_id
                FROM
                    levelupapi_event e
                JOIN 
                    levelupapi_game g ON g.id = e.game_id
                JOIN
                    levelupapi_gamerevent ge ON e.id = ge.event_id
                JOIN
                    auth_user u ON ge.gamer_id = u.id
            """)

            dataset = db_cursor.fetchall()

            # {
            #  1: {
            #      "gamer_id": 1,
            #      "full_name": "Molly Ringwald",
            #      "events": [
            #          {
            #              "id": 5,
            #              "date": "2020-12-23",
            #              "time": "19:00",
            #              "game_name": "Fortress America"
            #          }
            #      ]
            #  }
            #}

            events_by_user = {}

            for row in dataset:
                event = Event()
                event.description = row["description"]
                event.date = row["date"]
                event.time = row["time"]
                event.game = Game.objects.get(pk=row["game_id"])

                # Store the user's id
                uid = row["user_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current game to the `games` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_users_with_events = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/list_with_events.html'
        context = {
            'userevent_list': list_of_users_with_events
        }

        return render(request, template, context)
