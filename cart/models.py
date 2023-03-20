from django.db import models

# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=50)
    created_in = models.DateField()
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    value = models.FloatField()
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.name