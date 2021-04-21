from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    national_code = models.TextField(null=True)
