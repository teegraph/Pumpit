from .models import Human
from rest_framework import serializers


class HumanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ("avatar", "first_name", "second_name", "age", "gender")
