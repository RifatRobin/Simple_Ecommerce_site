from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Product, Contact, Order
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


def buynow(request):
    if request.method == "POST":

        firstName = request.POST.get('firstName', "")
        lastName = request.POST.get('lastName', "")
        Bemail = request.POST.get('Bemail', "")
        phone = request.POST.get('phone', "")
        pid = request.POST.get('pid', "")
        quantity = request.POST.get('quantity', "")
        city = request.POST.get('city', "")
        district = request.POST.get('district', "")
        address = request.POST.get('address', "")
        zipcode = request.POST.get('zipcode', "")

        orderdata = Order(firstName=firstName, lastName=lastName, Bemail=Bemail, zipcode=zipcode,
                          phone=phone, pid=pid, quantity=quantity, district=district, city=city, address=address)
        orderdata.save()
        passOrder = True
        oid = Order.order_id
        print(oid)
        return render(request, "shop/buynow.html", {'passOrder': passOrder, 'oid': oid})
    return render(request, "shop/buynow.html")


def search(request):
    queryset = request.GET['queryset']
    spd = Product.objects.filter(productName__icontains=queryset)
    spp = Product.objects.filter(price__icontains=queryset)
    spdp = spd.union(spp)
    sResult = {'spdp': spdp, 'queryset': queryset}
    return render(request, "shop/search.html", sResult)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "take another username")
                return render(request, 'shop/register.html')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return render(request, 'shop/register.html')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, email=email, password=password1)
                user.save()

        else:
            messages.info(request, "password Not macthed")
            return render(request, "shop/register.html")
        return redirect('/')
    else:
        return render(request, 'shop/register.html')


def login(request):
    return render(request, 'shop/login.html')


def logout(request):
    auth.logout(request)
    redirect("/")


def track(request):
    return render(request, "shop/deliveryStatus.html",)


def about(request):
    return render(request, "shop/a.html",)
