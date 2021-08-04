from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from decimal import Decimal

from .models import User, Listing


def index(request):
    return render(request, "cswebfunding/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cswebfunding/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "cswebfunding/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "cswebfunding/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "cswebfunding/register.html", {
                "message": "Username already taken."
            })

        user = User.objects.get(username=username)
        user.photo = request.FILES["photo"]
        user.about_me = request.POST["about_me"]
        user.save()

        login(request, user)

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "cswebfunding/register.html")


def addfunds(request, amount):
    # Convert amount from string to decimal
    amount = Decimal(amount)
    # Add amount to users current balance
    user = request.user
    user.balance = user.balance + amount
    user.save()
  
    return JsonResponse({"Message": f"{request.user.username} added {amount} to their balance"}, status=200)


def newlisting(request):

    # Go to newlisting Page
    if request.method == "GET":
        return render(request, "cswebfunding/newlisting.html")

    # Register a new listing
    elif request.method == "POST":

        # Get all the info needed and create a new listing
        if request.POST["type"] == "project":
            project = 1
            goodcause = 0
        elif request.POST["type"] == "goodcause":
            project = 0
            goodcause = 1
        else:
            print("Error")
            return render(request, "cswebfunding/index.html")
        
        listing = Listing(
            title = request.POST["title"],
            description = request.POST["description"],
            author = request.user,
            project = project,
            goodcause = goodcause,
            goal = request.POST["goal"], 
            final_date = request.POST["final_date"],
            category = request.POST["category"],
            photo = request.FILES["photo"]
        )
        
        listing.save()

        # Return to index page
        return render(request, "cswebfunding/index.html")
    else:
        return render(request, "cswebfunding/index.html")


def all_listings(request):
    
    listings = Listing.objects.all()

    return render(request, "cswebfunding/all_listings.html", {
        'listings': listings
    })


def listing (request, id):
    try:
        listing = Listing.objects.get(id=id)
    except ObjectDoesNotExist:
        listing = None

    return render(request, "cswebfunding/listing.html", {
        "listing": listing
    })


def profile (request, id):

    profile = User.objects.get(id=id)
    return render(request, "cswebfunding/profile.html", {
        "profile": profile
    })