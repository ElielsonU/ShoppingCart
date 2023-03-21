from django.shortcuts import render, redirect
from . import models
import datetime
# Create your views here.

def index(request):
    carts_list = models.Cart.objects.all()
    return render(request, "cart/index.html", {"carts_list" : carts_list })

def carts(request, id):

    cart = models.Cart.objects.get(id=id)

    items_list = models.Item.objects.filter(cart_id=id)
    context = { "cart": cart, "items_list": items_list, }        

    return render(request, "cart/carts.html", context)

def postCart(request):
    print(request.POST["name"])
    cart = models.Cart()
    cart.name = request.POST["name"]
    cart.created_in = datetime.datetime.now()
    cart.save()
    return redirect("/cart/%s"%cart.id)

def deleteCart(request, id):
    cart = models.Cart.objects.get(id=id)
    cart.delete()
    return redirect("/cart")

def postItem(request):
    cart = models.Cart.objects.get(id=request.POST["cart_id"])
    if request.method == "POST":
        item = models.Item()
        item.name = request.POST["name"]
        item.value = request.POST["value"]
        item.cart_id = cart
        item.save()
    return redirect("/cart/%s"%request.POST["cart_id"])

def deleteItem(request, id):
    item = models.Item.objects.get(id=id)
    cart_id = item.cart_id.id
    item.delete()
    return redirect("/cart/%s"%cart_id)

