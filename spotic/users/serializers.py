from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password', 'password_confirm']

    def validate(self, value):
        if value['password'] != value['password_confirm']:
            raise serializers.ValidationError('Пароли не совпадают')
        return value

    def validate_username(self, value):
        cleaned_username = value.strip()
        if not cleaned_username:
            raise serializers.ValidationError('Username не может быть пустым')
        if len(cleaned_username) < 3:
            raise serializers.ValidationError('Username не можут быть меньше 3 символов')
        return cleaned_username

    def validate_role(self, value):
        if value == 'singer':
            raise serializers.ValidationError('Для создания профиля исполнителя перейдите в создание songer')
        if value == 'admin':
            raise serializers.ValidationError('Вы не можете стать администратором')
        return value

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email', ''),
            password = validated_data['password']
        )
        return user


    def to_representation(self, instance):
        request = self.context.get('request')
        if request is None:
            return {
                'username': instance.username,
                'email': instance.email,
                'role': getattr(instance, 'role', ''), 
            }

        user = request.user

        if user.is_authenticated and hasattr(user, 'role'):
            if user.role == 'admin':
                return {
                    'id': instance.id,
                    'username': instance.username,
                    'email': instance.email,
                    'role': instance.role,
                }
            if user.role in ['songer', 'listener']:
                return {
                    'username': instance.username,
                    'email': instance.email,
                    'role': instance.role,
                }

        return {
            'username': instance.username,
            'email': instance.email,
        }
                
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        request = self.context['request'].user
        old_password = data.get('old_password')
        if not user.check_password(old_password):
            raise serializers.ValidationError({"old_password": "Старый пароль введен неверно."})
        if old_password == data.get('new_password'):
            raise serializers.ValidationError(
                {"new_password": "Новый пароль не может совпадать со старым."}
            )
        return data