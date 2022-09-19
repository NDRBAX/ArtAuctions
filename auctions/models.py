from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField


class User(AbstractUser):
    watchlist = models.ManyToManyField("Listing", blank=True, related_name="watchers") 
    pass
class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    description = models.TextField()
    artist = models.CharField(max_length=64, default="Unknown")
    year = models.IntegerField(default=0)
    size = models.CharField(max_length=64, default="Unknown")
    avatar = models.URLField(blank=True, default="https://static.vecteezy.com/system/resources/previews/004/141/669/original/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg", max_length=300)
    category = models.CharField(max_length=250, blank=True)             
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True)
    bid_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid = models.DecimalField(max_digits=10, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bid}"
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.comment}"

