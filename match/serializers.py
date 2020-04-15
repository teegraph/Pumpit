from .models import Match
from rest_framework import serializers
from human.serializers import HumanSerializers


class MatchSerializers(serializers.ModelSerializer):
    human = HumanSerializers(read_only=True)

    class Meta:
        model = Match
        fields = ("first_name", "second_name", "age", "gender", "human")
