from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product


def index(request):
    return render(request, 'shop/index.html')


def preview(request):
    products = Product.objects.all()
    return render(request, "shop/p.html", {"products": products})


def contact(request):
    return HttpResponse("Our Contact details is here")


def track(request):
    return HttpResponse("Track your product status")


def about(request):
    return HttpResponse("About our term & conditions")
