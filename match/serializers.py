from .models import Match
from rest_framework import serializers


class MatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ("first_name", "second_name", "age", "gender", "human_id")
