from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product, Contact
from math import ceil


def index(request):
    products = Product.objects.all()
    n = len(products)
    no_slide = n//2 + ceil((n/2)-(n//2))
    parameter = {"products": products,
                 "number_of_slides": no_slide, "range": range(1, no_slide)}
    return render(request, "shop/index.html", parameter)


def preview(request, p_id):
    # here id is the byDefault primaryKey to fetch the data in jango, if you didnot make one as primaryKey==True.
    prod = Product.objects.filter(id=p_id)
    print(prod)
    return render(request, "shop/productView.html", {"prod": prod[0]})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get("email", "")
        problem = request.POST.get("problem", "")
        contact_data = Contact(name=name, email=email, problem=problem)
        print(contact_data)
        contact_data.save()
    # problem_contact = Contact.objects.all()
    return render(request, "shop/contact.html")


def track(request):
    return render(request, "shop/d.html",)


def about(request):
    return render(request, "shop/a.html",)
