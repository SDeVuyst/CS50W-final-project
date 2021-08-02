
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.newlisting, name="newlisting"),
    path("all_listings", views.all_listings, name="all_listings"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("addfunds/<str:amount>", views.addfunds, name="addfunds"),
]
