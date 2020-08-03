from django.db import models
from django.contrib.auth.models import AbstractUser        #ABSTRACTUSER helps in creating custom user model


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
