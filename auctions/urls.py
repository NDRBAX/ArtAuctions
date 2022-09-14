from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create_listing"),
    path("new", views.create_new, name="new_listing"),
    path("auction/<int:id>", views.show_auction, name="show_auction"),
    path("add/<int:id>", views.new_comment, name="new_comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("edit_watchlist/<int:id>", views.edit_watchlist, name="edit_watchlist"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("close/<int:id>", views.close_auction, name="close"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),


]
