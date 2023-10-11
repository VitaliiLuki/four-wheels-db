from cars.models import Car, Option
from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CarSerializer, OptionGetSerializer


def index(request):
    text = '<h1> Если ты это видешь, то значит все работает! </h1>'
    return HttpResponse(text)


class CarsViewSet(viewsets.ModelViewSet):
    """Return a cars data to client"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionGetSerializer
