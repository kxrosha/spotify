from django.db import models
from users.models import User


class Singer(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    songs = models.ForeignKey('songs.Song', on_delete=models.CASCADE, related_name='songs')
    role = models.CharField(max_length=10, choices=User.Role.ROLE, default='singer')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Album(models.Model):
    user = models.ForeignKey('artists.Singer', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Альбом')
    description = models.CharField(blank=True, verbose_name='Описание')
    songs = models.ManyToManyField('songs.Song', related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

