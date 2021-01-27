from rest_framework import serializers
from levelupapi.models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'maker', 'number_of_players', 'skill_level', 'gametype')
        depth = 1
