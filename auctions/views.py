from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone

from .models import *
from .forms import *



def index(request):
    listing = Listing.objects.all().order_by('-created_at')
    listing_active = listing.filter(status=True)

    if request.user.is_authenticated:
        user_watchlist = request.user.watchlist.all().count()
        if user_watchlist > 0:
            watchlist = request.user.watchlist.all()
            total = watchlist.count()
        else:
            watchlist = None
            total = 0 
    else:
        watchlist = None
        total = None 

    return render(request, "auctions/index.html", {
        "listings": listing_active,
        "watchlist": watchlist,
        "total": total,
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
                "message": "Invalid username and/or password.",
                "cover_title": "Start selling and buying art now",
                "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform.\n If you don't have an account, please register."

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
                "message": "Passwords must match.",
                "cover_title": "Start selling and buying art now",
                "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform.\n If you don't have an account, please register."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken.",
                "cover_title": "Start selling and buying art now",
                "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform.\n If you don't have an account, please register."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html", {
            "cover_title": "Start selling and buying art now",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform.\n If you don't have an account, please register."
        })

# Create Listing Form 
def create_listing(request):
    if request.user.is_authenticated:
        user_watchlist = request.user.watchlist.all().count()
        if user_watchlist > 0:
            watchlist = request.user.watchlist.all()
            total = watchlist.count()
        else:
            watchlist = None
            total = 0
        return render(request, "auctions/create_listing.html", {
            "new_auction": ListingForm(),
            "total": total,
            "cover_title": "Sell your painting",
            "cover_description": "Please fill in the form below to sell your painting. Be sure to include all the details. If you add a picture, it will be displayed on the auction page and by the way it will be easier for the buyers to find your painting."
        })
    else:
        watchlist = None
        total = 0 
        return render(request, "auctions/login.html", {
            "total": total,
            "cover_title": "To create a listing you need to login",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform. If you don't have an account, please register."
        })

def create_new(request):
    if request.user.is_authenticated:
        form = ListingForm(request.POST)
        if form.is_valid():
            new_auction = Listing(seller = request.user, **form.cleaned_data)

            if new_auction.avatar == "":
                new_auction.avatar = "https://static.vecteezy.com/system/resources/previews/004/141/669/original/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg"

            new_auction.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_listing.html", {
                "new_auction": form,
                "cover_title": "You must select at least one category",
                "cover_description": "Please fill in the form below to sell your painting. Be sure to include all the details. If you add a picture, it will be displayed on the auction page and by the way it will be easier for the buyers to find your painting."
            })
    else:
        return render(request, "auctions/login.html", {
            "cover_title": "To create a listing you need to login",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform. If you don't have an account, please register.",

        })

# Show auction 
def show_auction(request, id):
    auction = Listing.objects.get(pk=id)

    if auction.status:
        if auction.bid_count > 0:
            highest_bid = Bid.objects.filter(listing = auction).order_by("-bid").first()
            if highest_bid:
                highest_bid = highest_bid.bid
                highest_bidder = Bid.objects.filter(listing = auction).order_by("-bid").first().bidder
            else:
                highest_bid = auction.open_price
                highest_bidder = None
        else:
            highest_bid = auction.open_price
            highest_bidder = None
    else:
        if auction.bid_count > 0:
            highest_bid = auction.price
            highest_bidder = Bid.objects.filter(listing = auction).order_by("-bid").first().bidder
        else:
            highest_bid = auction.open_price
            highest_bidder = None

    if request.user.is_authenticated:
        watchlist = request.user.watchlist.all()
        total = watchlist.count()
    else:
        watchlist = None
        total = None
    return render(request, "auctions/auction.html", {
        "auction": auction,
        "buyer": auction.buyer,
        "bid": highest_bid,
        "bidder": highest_bidder,
        "comments": Comment.objects.filter(listing = auction).order_by("-created_at"),
        "cover_title": auction.title,
        "cover_description": auction.description,
        "comment_form": CommentForm(),
        "bid_form": BidForm(),
        "watchlist":watchlist,
        "total":total
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
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform. If you don't have an account, please register."
        })

# Post bid
def bid(request, id):
    if request.user.is_authenticated:
        form = BidForm(request.POST)
        auction = Listing.objects.get(pk=id)
        if form.is_valid():
            if request.user == auction.seller:
                messages.error(request, "You can't bid on your own auction")
                return HttpResponseRedirect(reverse("show_auction", kwargs={
                    "id" : id
                    }))
            else:
                bid = request.POST["bid"]
                new_bid = Bid(bidder = request.user, listing = Listing.objects.get(pk=id) , **form.cleaned_data)
                starting_bid = Listing.objects.get(pk=id).open_price
                if "." in bid:
                    messages.error(request, "Please enter a whole number")
                    return HttpResponseRedirect(reverse("show_auction", kwargs={
                        "id" : id
                        }))
                if int(bid) >= int(starting_bid) + int(starting_bid) * 0.05:
                    new_bid.bidder, new_bid.bid = request.user, int(bid)
                    new_bid.save()
                    auction.bid_count += 1
                    auction.price = int(bid)
                    auction.save()
                    messages.success(request, "Your bid has been submitted")
                    return HttpResponseRedirect(reverse("show_auction", kwargs={
                        "id" : id
                        }))
                else:
                    if(auction.bid_count > 0):
                        price = Bid.objects.filter(listing = auction).order_by("-bid").first().bid
                    else:
                        price = auction.open_price
                   
                    allowed_bid = int(price) + int(price) * 0.05
                    allowed_bid = int(allowed_bid)
                    messages.error(request, f"Your bid must be at least 5% higher than the current price. The minimum bid is ${allowed_bid}")
                    return HttpResponseRedirect(reverse("show_auction", kwargs={
                        "id" : id
                        }))
        else:
            return render(request, "auctions/auction.html", {
                "bid_form": form,
            })
    else:
        return render(request, "auctions/login.html", {
            "cover_title": "To place a bid you need to login",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform. If you don't have an account, please register."
        })

# Close auction
def close_auction(request, id):
    if request.user.is_authenticated:
        auction = Listing.objects.get(pk=id)
        if request.user == auction.seller:
            auction.status = False
            if auction.bid_count == 0:
                auction.price = auction.open_price
                auction.buyer = None
                auction.updated_at = timezone.now()
            else:
                auction.price = Bid.objects.filter(listing = auction).order_by("-bid").first().bid
                auction.buyer = Bid.objects.filter(listing = auction).order_by("-bid").first().bidder
                auction.updated_at = Bid.objects.filter(listing = auction).order_by("-bid").first().created_at

            auction.save()
            messages.success(request, "Auction closed successfully")
            return HttpResponseRedirect(reverse("show_auction", kwargs={
                "id" : id
                }))

# Watchlist
def watchlist(request):

    if request.user.is_authenticated:
        watchlist = request.user.watchlist.all()
        watchlist = watchlist.order_by("-created_at")
        total = watchlist.count()
        if total == 0:
            cover_title = "Your watchlist is empty"
            cover_description = "Add auctions to your watchlist to keep track of them."
        else:
            cover_title = "Your watchlist"
            cover_description = "Here you can find all the auctions you're watching. You can add or remove auctions from your watchlist by clicking on the watchlist button on the auction page."

        return render(request, "auctions/watchlist.html", {
            "watchlist": watchlist,
            "total": total,
            "cover_title": cover_title,
            "cover_description": cover_description
        })
    else:
        return render(request, "auctions/login.html", {
            "cover_title": "To create a watchlist you need to login",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform. If you don't have an account, please register."
        })

def edit_watchlist(request, id):
    if request.user.is_authenticated:
        auction = Listing.objects.get(pk=id)
        user = request.user
        watchlist = user.watchlist.all()
        total = watchlist.count()
        print(total)
        if auction in watchlist:
            request.user.watchlist.remove(auction)
            
            user.save()
    
            return redirect(request.META['HTTP_REFERER'],{
                "watchlist": watchlist,
            })
        else:
            request.user.watchlist.add(auction)
            user.save()
              
            return redirect(request.META['HTTP_REFERER'], {
                "watchlist": watchlist,
            })
    else:
        return render(request, "auctions/login.html", {
            "cover_title": "To add an auction to your watchlist you need to login",
            "cover_description": "Create an account or login to your existing account to unlock the full potential of our platform. If you don't have an account, please register."
        })

# Categories
def categories(request):
    listing = Listing.objects.all().order_by('-created_at')
    categories = listing.values_list('category', flat=True).distinct()
    # splice categories
    categories = [x.split(",") for x in categories]
    # flatten list
    categories = [item for sublist in categories for item in sublist]
    # remove empty spaces
    categories = [x.strip() for x in categories]
    # remove duplicates
    categories = list(dict.fromkeys(categories))
    # sort alphabetically
    categories.sort()

    if request.user.is_authenticated:
        user_watchlist = request.user.watchlist.all().count()
        if user_watchlist > 0:
            watchlist = request.user.watchlist.all()
            total = watchlist.count()
        else:
            watchlist = None
            total = 0 
    else:
        watchlist = None
        total = None 
    
    return render(request, "auctions/categories.html", {
        "categories": categories,
        "total": total,
        "watchlist": watchlist,

        "listings": listing,
        "cover_title": "Categories",
        "cover_description": "Here you can find all the categories of our auctions. You can filter the auctions by category by clicking on the category button on the auction page."
    })

def category(request, category):
    auction = Listing.objects.all()
    categories = auction.values_list('category', flat=True).distinct()
    # splice categories
    categories = [x.split(",") for x in categories]
    # flatten list
    categories = [item for sublist in categories for item in sublist]
    # remove empty spaces
    categories = [x.strip() for x in categories]
    # remove duplicates
    categories = list(dict.fromkeys(categories))
    # sort alphabetically
    categories.sort()
    # show listing by category
    listing = Listing.objects.filter(category__icontains=category)

    if request.user.is_authenticated:
        user_watchlist = request.user.watchlist.all().count()
        if user_watchlist > 0:
            watchlist = request.user.watchlist.all()
            total = watchlist.count()
        else:
            watchlist = None
            total = 0 
    else:
        watchlist = None
        total = None 

    return render(request, "auctions/categories.html", {
        "listings": listing,
        "total": total,
        "watchlist": watchlist,
        "categories": categories,
        "category": category,
        "cover_title": category,
        "cover_description": "Here you can find all the auctions of the category " + category + ". You can filter the auctions by category by clicking on the category button on the auction page."
    })