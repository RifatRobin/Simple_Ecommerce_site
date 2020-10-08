from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "shop/index.html", {"products": products})


# def preview(request):
    # products = Product.objects.all()
    # return render(request, "shop/index.html", {"products": products})


def contact(request):
    return render(request, "shop/c.html",)


def track(request):
    return render(request, "shop/d.html",)


def about(request):
    return render(request, "shop/a.html",)
