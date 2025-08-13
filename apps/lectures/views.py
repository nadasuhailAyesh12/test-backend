from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Lecture
from .serializers import LectureSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


