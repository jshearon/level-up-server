from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Event(models.Model):
  description = models.TextField()
  date = models.DateField(null=True)
  time = models.TimeField(null=True)
  organizer = models.ForeignKey("Gamer",
    on_delete=CASCADE,
    related_name="events",
    related_query_name="event"
    )
  game = models.ForeignKey("Game",
    on_delete=CASCADE,
    related_name="events",
    related_query_name="event"
    )
  players = models.ManyToManyField("Gamer",
    related_name="player_events",
    related_query_name="player_event"
    ) 
  @property
  def joined(self):
    return self.__joined

  @joined.setter
  def joined(self, value):
    self.__joined = value
