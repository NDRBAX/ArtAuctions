from django.contrib import admin
from .models import *
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "year", "size", "category", "price", "open_price", "bid_count", "status", "buyer")
    list_filter = ("title", "artist", "year", "size", "category", "price", "open_price", "bid_count", "status", "buyer")
    search_fields = ("title", "artist", "year", "size", "category", "price", "open_price", "bid_count", "status", "buyer")
    list_per_page = 25

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "comment", "created_at")
    list_filter = ("user", "listing", "created_at")
    search_fields = ("user", "listing", "comment")
    ordering = ("user", "listing", "created_at")
    filter_horizontal = ()
    list_per_page = 25

class BidAdmin(admin.ModelAdmin):
    list_display = ("listing", "bidder", "bid", "created_at")
    list_filter = ("listing", "bidder", "created_at")
    search_fields = ("listing", "bidder", "bid")
    ordering = ("listing", "bidder", "created_at")
    filter_horizontal = ()
    list_per_page = 25

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    list_filter = ("username", "email")
    search_fields = ("username", "email")
    ordering = ("username", "email")
    filter_horizontal = ()
    list_per_page = 25

admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)


