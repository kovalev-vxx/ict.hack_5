from rest_framework import generics

from main_site.models import DefaultUser
from main_site.serializers import DefaultUserSerializer


class DefaultUserAPIViews(generics.CreateAPIView):
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserSerializer
    # def post(self, request, *args, **kwargs):

