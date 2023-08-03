from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework.authtoken.models import Token
from uuid import uuid4
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if password is None:
            raise TypeError('Senha deve ser definida')
        if not email:
            raise ValueError('O email é obrigatório.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.username = email
        user.set_password(password)
        user.save(using=self._db)

        user_obj = User.objects.get(email=email)
        return Token.objects.get_or_create(user=user_obj)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    birth = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(unique=True)
    first_login = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.username = self.email
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

        user_obj = User.objects.get(email=self.email)
        return Token.objects.get_or_create(user=user_obj)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        ordering = ['email']

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
