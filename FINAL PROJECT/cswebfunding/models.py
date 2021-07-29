from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
   # Balance can be maximum 999,999.99
   balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)

class Listing(models.Model):
   author = models.ForeignKey('User', on_delete=models.CASCADE)
   category = models.BooleanField()
   goal = models.PositiveIntegerField()
   creation_date = models