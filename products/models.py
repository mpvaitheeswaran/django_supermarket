from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='product_pics')
    stock = models.BooleanField(default=True)
    column = models.IntegerField(default=1)
    