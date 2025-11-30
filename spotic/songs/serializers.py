from .models import Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['songer', 'name', 'duration']


    def validate_name(self, value):
        symb = ['@#$%^&*()+']
        if not value:
            raise serializers.ValidationError('Название песни не может быть пустым')
        if value < 2:
            raise serializers.ValidationError('Название песни не может быть меньше 2 символов')
            if symb in value:
                raise serializers.ValidationError('Используйте для названия только буквы и цифры')
        return value