from rest_framework import serializers
from rest_framework import viewsets
from app.settings import DATETIME_FORMAT
from .models import User


class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT, input_formats=None)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'created')


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
