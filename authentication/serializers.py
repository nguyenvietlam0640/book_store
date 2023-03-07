from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = [
            'id',
            'full_name',
            'email',
            'password',
            'phone',
            'birthday',
            'creation_date',
            'get_absolute_url',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }


