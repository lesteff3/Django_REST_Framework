from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    if_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username