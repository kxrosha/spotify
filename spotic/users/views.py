from django.shortcuts import render
from rest_framework import permissions, generics, status
from .models import User
from .serializers import UserSerializer, UserUpdateDeleteSerializer, UpdatePasswordSerializer
from .permissions import IsAdmin, IsSongerOrAdnin, IsListener
from rest_framework.response import Response


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class RetrieveUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class DeleteUserView(generics.DestroyAPIView):
    serializer_class = UserUpdateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    

class UpdatePasswordView(generics.GenericAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'detail': 'пароль успешно изменен'}, status=status.HTTP_200_OK
        )

