from rest_framework import serializers

from users.models import User

class UserCreationsSerializer(serializers.ModelSerializer):
    """
    Serializer to create user with fields
    - email
    - name
    - surname
    - password
    - birthday (optional)
    - phone (optional)
    """

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'birthdate', 'phone']
        extra_kwargs = {'password': {'write_only': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True},
                        'birthdate': {'required': False},
                        'phone': {'required': False}}


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve user with fields
    - name
    - surname
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        extra_kwargs = {
                        'first_name': {'required': True},
                        'last_name': {'required': True},}

