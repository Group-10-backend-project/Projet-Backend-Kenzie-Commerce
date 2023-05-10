from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if 'password' in validated_data:
            new_password = validated_data.pop('password')
            instance.set_password(new_password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'is_seller',
            'is_superuser',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {
                'validators': [UniqueValidator(
                    queryset=User.objects.all(),
                    message='Username already exists.',
                )]
            },
            'email': {
                'validators': [UniqueValidator(
                    queryset=User.objects.all(),
                    message='E-mail already registered.',
                )]
            },
        }
