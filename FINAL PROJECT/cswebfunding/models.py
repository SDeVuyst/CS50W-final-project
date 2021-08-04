from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
   # Balance can be maximum 999,999.99
   balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
   photo = models.ImageField(upload_to='media/', default="default-user.jpg")
   about_me = models.CharField(max_length=256, default="Description of User")


class Listing(models.Model):
   title = models.CharField(max_length=50)
   description = models.CharField(max_length=256)
   author = models.ForeignKey('User', on_delete=models.CASCADE)
   project = models.BooleanField(default=0)
   goodcause = models.BooleanField(default=0)
   donated = models.PositiveIntegerField(default=0)
   category = models.PositiveIntegerField(default=9)
   goal = models.PositiveIntegerField(validators=[MaxValueValidator(10000000),MinValueValidator(10)])
   amountbackers = models.PositiveIntegerField(default=0)
   created_at = models.DateField(auto_now_add=True)
   final_date = models.DateField()
   photo = models.ImageField(upload_to='media/', default="default-listing.jpg")