from django.contrib import admin
from .models import *
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "seller", "category", "price", "bid_count", "status", "buyer")
    list_filter = ("seller", "category", "status", "buyer")
    search_fields = ("title", "seller", "category", "buyer")
    ordering = ("title", "seller", "category", "price", "bid_count", "status", "buyer")
    filter_horizontal = ()
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)