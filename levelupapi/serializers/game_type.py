from rest_framework import serializers
from levelupapi.models import GameType

class GameTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameType
        url = serializers.HyperlinkedIdentityField(
            view_name='gametype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'label')
