from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role():
        ROLE = (
            ('admin', 'администратор'), 
            ('songer', 'исполнитель'),
            ('listener', 'слушатель')
        )

    role = models.CharField(max_length=15, choices=Role.ROLE, default='listener')
    
    def __str__(self):
        return self.username
    