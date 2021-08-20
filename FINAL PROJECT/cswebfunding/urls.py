from django.urls import path
import notifications.urls
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.newlisting, name="newlisting"),
    path("listing/<int:id>", views.listingfunc, name="listing"),
    path("addfunds/<str:amount>", views.addfunds, name="addfunds"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("listings/<str:filter>", views.listings, name="listings"),
    # API 
    path("donate", views.donate, name="donate"),
    path('comment', views.comment, name="comment"),
    path('removecomment', views.removecomment, name="removecomment"),
    # https://github.com/django-notifications/django-notifications
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('readnoti', views.readnoti, name="readnoti"),

]
