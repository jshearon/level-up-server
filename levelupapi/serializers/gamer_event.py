from rest_framework import serializers
from levelupapi.models import Gamer
from levelupapi.serializers import EventUserSerializer

class GamerEventSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = EventUserSerializer(many=False)

    class Meta:
        model = Gamer
        fields = ['user']
