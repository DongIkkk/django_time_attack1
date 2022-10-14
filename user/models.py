from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = "myuser"

    phone_number = models.CharField(max_length=20, default='')
    address = models.TextField()

