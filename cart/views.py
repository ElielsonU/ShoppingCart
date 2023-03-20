from django.shortcuts import render, redirect
from . import models
import datetime
# Create your views here.

def index(request):
    return render(request, "cart/index.html")

def postCart(request):
    print(request.POST["name"])
    cart = models.Cart()
    cart.name = request.POST["name"]
    cart.created_in = datetime.datetime.now()
    cart.save()
    return redirect("/")


