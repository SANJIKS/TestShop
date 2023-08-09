from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        write_only_fields = ['password']
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Такая почта уже существует!')
        return email

    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField() # Используйте username вместо email
    password = serializers.CharField()

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Пользователь с таким именем пользователя не найден')
        return username

    def validate(self, attrs):
        request = self.context.get('request')
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(username=username, password=password, request=request)
            if not user:
                raise serializers.ValidationError('Неправильно указан username или пароль')
        else:
            raise serializers.ValidationError('username и пароль обязательны к заполнению')
        attrs['user'] = user
        return attrs
