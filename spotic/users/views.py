from django.shortcuts import render
from rest_framework import permissions, generics
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin, IsSongerOrAdnin, IsListener


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class DestroyDetailUpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.ojects.filter(id=self.request.user.id)
    
