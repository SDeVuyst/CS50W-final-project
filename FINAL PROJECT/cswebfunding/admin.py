from django.contrib import admin
from .models import User, Listing, Donation, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Donation)
admin.site.register(Comment)