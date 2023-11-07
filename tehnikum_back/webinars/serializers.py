from rest_framework import serializers

from .models import Webinars


class WebinarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinars
        fields = "__all__"
