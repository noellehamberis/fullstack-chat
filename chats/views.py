from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers
# Create your views here.


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = models.Message.objects.all().order_by('created_at')
    serializer_class = serializers.MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
