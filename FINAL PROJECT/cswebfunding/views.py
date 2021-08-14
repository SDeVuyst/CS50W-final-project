from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from decimal import Decimal

from .models import User, Listing, Donation, Comment


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


def listing(request, id, message=''):
    try:
        listing = Listing.objects.get(id=id)
    except ObjectDoesNotExist:
        listing = None

    if "success" in message:
        amount = message.replace("success", '')
        message = f"You have succesfully donated ${amount}!"

    elif message == "comment":
        message = "Commented Successfully!"
    # Add 1 popularity per view
    listing.popularity += 1
    listing.save()

    return render(request, "cswebfunding/listing.html", {
        "listing": listing,
        "message": message        
    })


def profile(request, id):


    profile = User.objects.get(id=id)
    return render(request, "cswebfunding/profile.html", {
        "profile": profile
    })


def listings(request, filter):

    # I hate the next 50 lines of code 
    if filter == 'goodcauses':
        listings = Listing.objects.filter(goodcause=1).order_by('-id')
        title = "Good Causes"

    elif filter == 'projects':
        listings = Listing.objects.filter(project=1).order_by('-id')
        title = "Projects"

    elif filter == 'latest':
        listings = Listing.objects.all().order_by('-id')
        title = "Latest Listings"

    elif filter == 'newest':
        listings = Listing.objects.all().order_by('id')
        title = "Newest Listings"

    elif filter == 'highest':
        listings = Listing.objects.all().order_by('-goal')
        title = "Listings With Highest Goal"

    elif filter == 'lowest':
        listings = Listing.objects.all().order_by('goal')
        title = "Listings With Lowest Goal"

    elif filter == 'art':
        listings = Listing.objects.filter(category=1).order_by('-id')
        title = "Art Listings"

    elif filter == 'comics-and-illustration':
        listings = Listing.objects.filter(category=2).order_by('-id')
        title = "Comics And Illustration listings"
    
    elif filter == 'design-and-tech':
        listings = Listing.objects.filter(category=3).order_by('-id')
        title = "Design And Tech Listings"
        
    elif filter == 'film':
        listings = Listing.objects.filter(category=4).order_by('-id')
        title = "Film Listings"
        
    elif filter == 'food-and-craft':
        listings = Listing.objects.filter(category=5).order_by('-id')
        title = "Food And Craft Listings"
        
    elif filter == 'games':
        listings = Listing.objects.filter(category=6).order_by('-id')
        title = "Games Listings"
        
    elif filter == 'music':
        listings = Listing.objects.filter(category=7).order_by('-id')
        title = "Music Listings"
        
    elif filter == 'publishing':
        listings = Listing.objects.filter(category=8).order_by('-id')
        title = "Publishing Listings"
    
    elif filter == 'other':
        listings = Listing.objects.filter(category=9).order_by('-id')
        title = "Other Listings"
        
    else: 
        return render(request, "cswebfunding/index.html")


    # Add Paginator
    paginator = Paginator(listings, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "cswebfunding/listings.html", {
        'title': title,
        'listings': page_obj
    })


def donate(request):

    if request.method == "POST":
        
        # Get amount and listing from form
        user = request.user
        amount = Decimal(request.POST["donateamount"])
        listingid = request.POST["listingid"]
        try:
            listing = Listing.objects.get(id=listingid)
        except:
            raise Exception("Listing Doesn't exist")

        # Check if user can afford the donation
        if user.balance < amount:
            raise Exception("User cannot afford donation")

        # Add donation model 
        donation = Donation(
            user=user,
            listing=listing,
            amount=amount
        )
        donation.save()

        # Deduct donation from balance
        user.balance -= amount
        user.save()

        # Add donation to listing
        listing.donated += amount
        listing.save()

        return redirect(f'/listing/{listingid}/success{amount}')

    else:
        raise Exception('WrongRequest')


def comment(request):

    if request.method == 'POST':
        try:
            id = request.POST["id"]
            content = request.POST["content"]
            listing = Listing.objects.get(id=id)
            
            # Add 5 popularity per comment
            listing.popularity += 5
            listing.save()
            
        except ObjectDoesNotExist:
            raise Exception("Listing not found...")

        # Actually create comment
        comment = Comment(
            listing = listing,
            user = request.user,
            content = content,
        )
        comment.save()

        return redirect(f'/listing/{id}/comment')

    else: 
        raise Exception("Wrong request method")