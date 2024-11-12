from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password', 'password_confirmation']

    def validate(self, data):
        # Проверка совпадения паролей
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Пароли не совпадают")

        # Проверка уникальности email
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует")

        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Принудительно используем email как имя пользователя для аутентификации
        user = authenticate(username=email, password=password)

        # Логирование для отладки
        if not user:
            print(f"Authentication failed for email: {email} with password: {password}")
            raise serializers.ValidationError("Неверные учетные данные")

        data['user'] = user
        return data

    def create(self, validated_data):
        user = validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return {"token": token.key}


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordVerifySerializer(serializers.Serializer):
    reset_code = serializers.CharField(max_length=100)


class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        # Проверка на совпадение нового пароля и его подтверждения
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"new_password": "Пароли не совпадают."})
        return attrs
