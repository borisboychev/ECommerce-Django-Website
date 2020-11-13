from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    UNKNOWN = 'unknown'

    GENDER_TYPES = (
        (MALE, 'male'),
        (FEMALE,'female'),
        (OTHER, 'other'),
        (UNKNOWN, 'unknown'),
    )

    name = models.CharField(max_length=60, default='ANONYMOUS')
    email = models.EmailField(max_length=250, unique=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=GENDER_TYPES, default=UNKNOWN)
    address = models.CharField(max_length=250, blank=True, null=True)

    session_token = models.CharField(max_length=32, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=30)
#     email = models.EmailField(max_length=250)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'User: {self.username} - {self.first_name} {self.last_name}'
