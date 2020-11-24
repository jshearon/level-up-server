from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
  title = models.CharField(max_length=75, default=None)
  maker = models.CharField(max_length=75, default=None)
  gamer = models.ForeignKey("Gamer", 
    on_delete=CASCADE,
    related_name="games",
    related_query_name="game")
  gametype = models.ForeignKey("GameType",
    on_delete=CASCADE,
    related_name="games",
    related_query_name="game")
  number_of_players = models.IntegerField()
  skill_level = models.IntegerField(default=0)
