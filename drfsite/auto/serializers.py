from rest_framework import serializers
from auto.models import Auto


class AutoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Auto
        fields = "__all__"

