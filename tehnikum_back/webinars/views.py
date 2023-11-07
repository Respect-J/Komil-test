from .models import Webinars
from .serializers import WebinarsSerializer
from rest_framework import generics


class WebinarsGet(generics.ListAPIView):
    queryset = Webinars.objects.all()
    serializer_class = WebinarsSerializer

