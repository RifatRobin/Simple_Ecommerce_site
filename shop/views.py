from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    n = len(products)
    no_slide = n//3+ceil((n/3)-(n//3))
    parameter = {"products": products,
                 "number_of_slides": no_slide, "range": range(1, no_slide)}
    return render(request, "shop/index.html", parameter)


# def preview(request):
    # products = Product.objects.all()
    # return render(request, "shop/index.html", {"products": products})


def contact(request):
    return render(request, "shop/c.html",)


def track(request):
    return render(request, "shop/d.html",)


def about(request):
    return render(request, "shop/a.html",)
