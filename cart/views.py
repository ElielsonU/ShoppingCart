from django.shortcuts import render, redirect
from . import models
import datetime
# Create your views here.

def index(request):
    carts_list = models.Cart.objects.all()
    return render(request, "cart/index.html", {"carts_list" : carts_list })

def carts(request, id):
    request.method
    cart = models.Cart.objects.get(id=id)
    items_list = models.Item.objects.filter(cart_id=id)
    
    context = {
        "cart": cart,
        "items_list": items_list,
    }

    return render(request, "cart/carts.html", context)

def postCart(request):
    print(request.POST["name"])
    cart = models.Cart()
    cart.name = request.POST["name"]
    cart.created_in = datetime.datetime.now()
    cart.save()
    return redirect("/")


