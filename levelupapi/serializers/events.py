from rest_framework import serializers
from rest_framework.serializers import StringRelatedField
from levelupapi.models import Event
from levelupapi.serializers import GameSerializer

class EventSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for events"""
    organizer = StringRelatedField()
    game = GameSerializer(many=False)

    class Meta:
        model = Event
        url = serializers.HyperlinkedIdentityField(
            view_name='event',
            lookup_field='id'
        )
        fields = ('id', 'url', 'game', 'organizer',
                  'description', 'date', 'time', 'joined')
