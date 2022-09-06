from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
        "cover_title" : "Discover hundreds of paintings",
        "cover_description" : " 789,900 artists and 15,140,400 auction prices, 1,008,800 artworks listed for the past 12 months, from 6,400 auction houses around the world."
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."

            })
    else:
        return render(request, "auctions/login.html", {
            "cover_title": "Start selling and buying art now",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform.\n If you don't have an account, please register."
        })


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html", {
            "cover_title": "Start selling and buying art now",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform.\n If you don't have an account, please register."
        })


# Create Listing
@login_required(login_url='auctions/login.html')
def create_listing(request):
    return render(request, "auctions/create_listing.html", {
        "form": ListingForm(),
        "cover_title": "Sell your painting",
        "cover_description": "Please fill in the form below to sell your painting. Be sure to include all the details. If you add a picture, it will be displayed on the auction page and by the way it will be easier for the buyers to find your painting."
    })

@login_required(login_url='auctions/login.html')
def create_new(request):
    form = ListingForm(request.POST)
    if form.is_valid():
        new_auction = Listing(seller = request.user, **form.cleaned_data)
        new_auction.save()
        open_price = new_auction.open_price
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_listing.html", {
            "form": form,

        })

# Show auction 
def show_auction(request, id):
    auction = Listing.objects.get(pk=id)
    return render(request, "auctions/auction.html", {
        "auction": auction,
        "buyer": auction.buyer,
        "comments": Comment.objects.filter(listing = auction),
        "cover_title": auction.title,
        "cover_description": auction.description,
        "comment_form": CommentForm(),
    })

# Post comment
def new_comment(request, id):
    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(user = request.user, listing = Listing.objects.get(pk=id) , **form.cleaned_data)
            new_comment.save()
            return HttpResponseRedirect(reverse("show_auction", kwargs={
                "id" : id
                }))
        else:
            return render(request, "auctions/auction.html", {
                "comment_form": form,
            })
    else:
        return render(request, "auctions/login.html", {
            "cover_title": "To add a comment you need to login",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform.\n If you don't have an account, please register."
        })


