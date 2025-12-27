from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phno = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
    


class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adminno = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username    
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    taxpercent = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name    
# Create your models here.
