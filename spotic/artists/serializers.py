from rest_framework import serializers
from .models import Singer, Album
from songs.serializers import SongSerializer
from songs.models import Song

class SongerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['user', 'description', 'songs', 'create_at']


    def validate(self, value):
        user = self.context['request'].user
        if Artist.objects.filter(user=user).exists():
            raise serializers.ValidationError(
                {"detail": "У вас уже есть карточка музыканта. Используйте PATCH для обновления."}
            )
        return value

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = ['user.username', 'name', 'description', 'songs', 'created_at']

    def create(self, validated_data):
        songs_data = validated_data.pop('songs')
        album = Album.objects.create(**validated_data)
        for song in songs_data:
            Song.objects.create(album=album, **song)
        return album