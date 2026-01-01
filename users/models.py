from django.db import models
from django.contrib.auth.models import AbstractUser
from .roles import Roles

class User(AbstractUser):
    name = models.CharField("name", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    first_name = None
    last_name = None

    role = models.CharField(
        max_length=20,
        choices=Roles.CHOICES,
        default=Roles.USER
    )

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name or self.username

    # def get_full_name(self):
    #     return self.name or self.username

    # def get_short_name(self):
    #     return self.name or self.username