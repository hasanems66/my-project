from django.db import models

# Create your models here.
from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()
    address = models.TextField(blank=True,null=True)




class DiscountCode(models.Model):
    name = models.CharField(max_length=10, unique=True)
    discount_percent = models.SmallIntegerField(default=0)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.name