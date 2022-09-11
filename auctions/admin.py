from django.contrib import admin
from .models import *
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "seller", "price", "open_price", "bid_count", "created_at", "updated_at", "status", "buyer")
    list_filter = ("seller", "created_at", "updated_at", "status", "buyer")
    search_fields = ("title", "seller", "price", "open_price", "bid_count", "created_at", "updated_at", "status", "buyer")
    ordering = ("title", "seller", "price", "open_price", "bid_count", "created_at", "updated_at", "status", "buyer")
    filter_horizontal = ()
    fieldsets = ()

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


