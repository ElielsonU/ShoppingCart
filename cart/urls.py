from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.carts),
    path("new", views.postCart),
]