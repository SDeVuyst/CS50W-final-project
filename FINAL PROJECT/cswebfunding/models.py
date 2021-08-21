from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
   id = models.BigAutoField(primary_key=True)
   # Balance can be maximum 999,999.99
   balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
   photo = models.ImageField(upload_to='media/', default="default-user.jpg")
   about_me = models.CharField(max_length=256, default="Description of User")

   def __str__(self):
      return f'{self.username}({self.id})'


class Listing(models.Model):
   id = models.BigAutoField(primary_key=True)
   title = models.CharField(max_length=50)
   description = models.CharField(max_length=256)
   author = models.ForeignKey('User', on_delete=models.CASCADE)
   project = models.BooleanField(default=0)
   goodcause = models.BooleanField(default=0)
   donated = models.PositiveIntegerField(default=0)
   category = models.PositiveIntegerField(default=9)
   goal = models.PositiveIntegerField(validators=[MaxValueValidator(10000000),MinValueValidator(10)])
   created_at = models.DateField(auto_now_add=True)
   final_date = models.DateField()
   photo = models.ImageField(upload_to='media/', default="default-listing.jpg")
   popularity = models.IntegerField(default=0)
   closed = models.BooleanField(default=0)

   def get_percentage(self):
        perc = self.donated * 100 / self.goal
        return perc

   def __str__(self):
      return f'{self.title}({self.id})'

   
class Donation(models.Model):
   id = models.BigAutoField(primary_key=True)
   user = models.ForeignKey('User', on_delete=models.CASCADE)
   listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
   amount = models.PositiveIntegerField(default=0)
   
   def __str__(self):
      return f'{self.user} donated ${self.amount} to {self.listing}'


class Comment(models.Model):
   id = models.BigAutoField(primary_key=True)
   listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
   user = models.ForeignKey('User', on_delete=models.CASCADE)
   content = models.TextField()
   date = models.DateField(auto_now_add=True)

   def __str__(self):
      return f'Comment {self.id}'