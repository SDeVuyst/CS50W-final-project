from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
   # Balance can be maximum 999,999.99
   balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)


class Listing(models.Model):
   title = models.CharField(max_length=50)
   description = models.CharField(max_length=256)
   author = models.ForeignKey('User', on_delete=models.CASCADE)
   project = models.BooleanField(default=0)
   goodcause = models.BooleanField(default=0)
   goal = models.PositiveIntegerField()
   amountbackers = models.PositiveIntegerField(default=0)
   created_at = models.DateTimeField(auto_now_add=True)
   final_date = models.DateField()
   photo = models.ImageField(upload_to='media/', default="default.jpg")