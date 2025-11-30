from django.db import models


class Song(models.Model):
    songer = models.ForeignKey('artists.Singer', on_delete=models.CASCADE, verbose_name='Исполнитель')
    name = models.CharField(max_length=50, verbose_name='Название песни')
    duration = models.DurationField(verbose_name='время')

    def __str__(self):
        return f'artist {self.songer.username} - song name: {self.name}'
    