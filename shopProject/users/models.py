from django.db import models
from django.contrib.auth.models import AbstractUser


from users.managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    birthdate = models.DateField("birthday", null=True)
    phone = models.CharField("phone number", max_length=20, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager() 

    def __str__(self) -> str:
        return self.email