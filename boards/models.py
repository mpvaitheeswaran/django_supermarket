from django.db import models
from django.db.models.fields import IntegerField
from products.models import Product

# Create your models here.
class Board(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE)