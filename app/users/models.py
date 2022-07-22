from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_active') is not True:
            raise ValueError('Superuser must be active')
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must be staff')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
