from rest_framework import serializers

from main_site.models import DefaultUser


class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = "__all__"
