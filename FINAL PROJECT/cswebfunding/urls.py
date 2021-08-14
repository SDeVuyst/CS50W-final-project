
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.newlisting, name="newlisting"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("listing/<int:id>/<str:message>", views.listing, name="listingdonated"),
    path("addfunds/<str:amount>", views.addfunds, name="addfunds"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("listings/<str:filter>", views.listings, name="listings"),
    path("donate", views.donate, name="donate"),
    path('comment', views.comment, name="comment")
]
