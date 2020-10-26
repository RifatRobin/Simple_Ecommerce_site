from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("", views.index, name="shome"),
    path("pre/<int:p_id>", views.preview, name="Preview"),
    path("con/", views.contact, name="Contact"),
    path("buynow/", views.buynow, name="Buynow"),
    path("tra/", views.track, name="Track"),
    path("abt/", views.about, name="About"),
]
