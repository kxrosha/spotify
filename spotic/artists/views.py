from django.shortcuts import render
from users.permissions import IsSonger
from rest_framework import generics, permissions
from .serializers import SongerSerializer, AlbumSerializer
from .models import Singer, Album
from rest_framework.response import Response
from django.db import IntegrityError


    # МУЗЫКАНТЫ
class CreateArtistsView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SongerSerializer
    queryset = Singer.objects.all()

    def perform_create(self, serializer):
        artist = serializer.save(user=self.request.user)
        user = self.request.user
        if user.role != 'songer':
            user.role = 'songer'
            user.save(update_fields=['role'])

class ListArtistsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SongerSerializer
    queryset = Singer.objects.all()

class RetrieveUpdateDeleteArtistsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SongerSerializer


    # АЛЬБОМЫ
class CreateAlbumView(generics.CreateAPIView):
    permission_classes = [IsSonger]
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListAlbumsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class UpdateAlbumView(generics.UpdateAPIView):
    permission_classes = [IsSonger]
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class RetrieveAlbumView(generics.RetrieveAPIView):
    permission_classes = [IsSonger]
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class DeleteAlbumView(generics.DestroyAPIView):
    permission_classes = [IsSonger]
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

