from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import SongSerializer
from users.permissions import IsSonger
from .models import Song


class CreateSongView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsSonger]

class ListSongView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetrieveSongView(generics.RetrieveAPIView):
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Song.objects.filter(id=self.request.song.id)

class UpdateSongView(generics.UpdateAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsSonger]

    def get_queryset(self):
        return Song.objects.filter(id=self.request.song.id)

class DeleteSongView(generics.DestroyAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsSonger]

    def get_queryset(self):
        return Song.objects.filter(id=self.request.song.id)

    