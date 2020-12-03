from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("", views.index, name="shome"),
    path("pre/<int:p_id>", views.preview, name="Preview"),
    path("con/", views.contact, name="Contact"),
    path("buynow/", views.buynow, name="Buynow"),
    path("search/", views.search, name="search"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("tra/", views.track, name="Track"),
    path("abt/", views.about, name="About"),
]
