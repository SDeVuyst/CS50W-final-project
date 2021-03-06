from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from notifications.signals import notify

from decimal import Decimal
import json

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


def listingfunc(request, id):

    try:
        listing = Listing.objects.get(id=id)
        print(listing.check_final_date())

        # Listing cannot be closed
        if listing.closed == True:
            raise Exception("Listing is closed")

    except ObjectDoesNotExist:
        raise Exception('Listing does not exist')

    # Add 1 popularity per view
    listing.popularity += 1
    listing.save()

    # Get all comments on that listing
    comments = Comment.objects.filter(listing=listing).order_by('-id')

    
    return render(request, "cswebfunding/listing.html", {
        "listing": listing,
        "comments": comments
    })


def profile(request, id):

    try:
        profile = User.objects.get(id=id)
        listings = Listing.objects.filter(author=profile).order_by('-id')
        comments = Comment.objects.filter(user=profile).order_by('-id')[:3]
    except:
        raise Exception("Something went wrong... Try again later")

    return render(request, "cswebfunding/profile.html", {
        "profile": profile,
        "listings": listings,
        "comments": comments,
    })


def listings(request, filter):

    # I hate the next 50 lines of code 
    if filter == 'goodcauses':
        listings = Listing.objects.filter(goodcause=1).filter(closed=0).order_by('-id')
        title = "Good Causes"

    elif filter == 'projects':
        listings = Listing.objects.filter(project=1).filter(closed=0).order_by('-id')
        title = "Projects"

    elif filter == 'all':
        listings = Listing.objects.all().order_by('-id')
        title = "All Listings"

    elif filter == 'latest':
        listings = Listing.objects.filter(closed=0).order_by('id')
        title = "Oldest Listings"

    elif filter == 'newest':
        listings = Listing.objects.filter(closed=0).order_by('-id')
        title = "Newest Listings"

    elif filter == 'highest':
        listings = Listing.objects.filter(closed=0).order_by('-goal')
        title = "Listings With Highest Goal"

    elif filter == 'lowest':
        listings = Listing.objects.filter(closed=0).order_by('goal')
        title = "Listings With Lowest Goal"

    elif filter == 'art':
        listings = Listing.objects.filter(category=1).filter(closed=0).order_by('-id')
        title = "Art Listings"

    elif filter == 'comics-and-illustration':
        listings = Listing.objects.filter(category=2).filter(closed=0).order_by('-id')
        title = "Comics And Illustration listings"
    
    elif filter == 'design-and-tech':
        listings = Listing.objects.filter(category=3).filter(closed=0).order_by('-id')
        title = "Design And Tech Listings"
        
    elif filter == 'film':
        listings = Listing.objects.filter(category=4).filter(closed=0).order_by('-id')
        title = "Film Listings"
        
    elif filter == 'food-and-craft':
        listings = Listing.objects.filter(category=5).filter(closed=0).order_by('-id')
        title = "Food And Craft Listings"
        
    elif filter == 'games':
        listings = Listing.objects.filter(category=6).filter(closed=0).order_by('-id')
        title = "Games Listings"
        
    elif filter == 'music':
        listings = Listing.objects.filter(category=7).filter(closed=0).order_by('-id')
        title = "Music Listings"
        
    elif filter == 'publishing':
        listings = Listing.objects.filter(category=8).filter(closed=0).order_by('-id')
        title = "Publishing Listings"
    
    elif filter == 'other':
        listings = Listing.objects.filter(category=9).filter(closed=0).order_by('-id')
        title = "Other Listings"
    
    elif filter =='popularity':
        listings = Listing.objects.filter(closed=0).order_by('popularity')
        title = "Popularity"
    
    elif filter == 'search':
        try:
            filter = request.POST['search']
        except:
            raise Exception('No searchbar found')

        listings = Listing.objects.filter(title__contains=filter)
        title = f"Search results for: {filter}"
        
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
        
        try:
            data = json.loads(request.body.decode('utf-8'))
            listingid = data["listingid"]
            amount = Decimal(data["amount"])
            listing = Listing.objects.get(id=listingid)
            user = request.user
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

        # Notify recipient
        notify.send(sender=user, recipient=listing.author, verb=f"{request.user.username} donated ${amount} to your listing!", authorurl=user.photo.url)

        return JsonResponse({"Message": "Donation registered!"}, status=200)

    else:
        raise Exception('Wrong Request method')


def comment(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            id = data["listingid"]
            content = data["content"]
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

        # Notify recipient
        notify.send(sender=request.user, recipient=listing.author, verb=f"{request.user.username} commented on your listing!", authorurl=request.user.photo.url)

        return JsonResponse({"message": "Comment added",
                             "imgsource": request.user.photo.url,
                             "username": request.user.username,
                             "comment": content,
                             "date": comment.date,
                             "commentid": comment.id
                             }, status=200)

    else: 
        raise Exception("Wrong request method")


def removecomment (request):

    if request.method == 'POST':

        # Get the commentid
        data = json.loads(request.body.decode('utf-8'))
        id = data["commentid"]
        print(id)

        # Delete the comment
        try:
            Comment.objects.get(id=id).delete()
        except:
            raise Exception("Comment not found...")

        return JsonResponse({"Message": "Comment removed"}, status=200)
    else:
        raise Exception("Wrong request method")


def readnoti (request):

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data["notification_id"]

        try:
            request.user.notifications.get(pk=id).mark_as_read()
        except:
            raise Exception("Notification not found...")

        return JsonResponse({"message": "Notification read"}, status=200)
    else:
        raise Exception("Wrong request method")


def closelisting (request):

    if request.method == 'POST':

        try:
            data = json.loads(request.body.decode('utf-8'))
            listingid = data["listingid"]

            listing = Listing.objects.get(id=listingid)
            listing.closed = True
            listing.save()

            notify.send(sender=request.user, recipient=request.user, verb=f"Your listing '{listing.title} was closed.", authorurl=request.user.photo.url)

        except:
            raise Exception("Something wrent wrong... Try again later.")

        return JsonResponse({"message": "Listing closed"}, status=200)
    else:
        raise Exception('Wrong request method')

