from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
  name = models.CharField(max_length=50)
  gamer = models.ForeignKey("Gamer", 
    on_delete=CASCADE,
    related_name="games",
    related_query_name="game")
  game_type = models.ForeignKey("GameType",
    on_delete=CASCADE,
    related_name="games",
    related_query_name="game")
  max_players = models.IntegerField()
