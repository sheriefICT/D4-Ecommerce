from collections.abc import Iterable
from django.db import models
import datetime
from django.contrib.auth.models import User
from product.models import Product
from utils.generate_code import Generate_code
from django.utils import timezone


CART_STATUS = (
    ('InPrograss','InPrograss'),
    ('Complate','Complate')
)

class Cart(models.Model):
    user = models.ForeignKey(User , related_name='cart_user',on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=CART_STATUS)
    def __str__(self):
        return str(self.user)  
    
    def cart_total(self):
        total = 0
        for item in self.cart_detale.all():
            total += item.total
        return round(total, 2)  

class CartDetale(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detale', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True, blank=True)
    def __str__(self):
        return str(self.cart)

 
ORDER_STATUS = (
    ('Resieved','Resieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'), 
)

class Order(models.Model):
    user = models.ForeignKey(User , related_name='order_user',on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS)
    code = models.CharField(max_length=10,default=Generate_code())
    order_time = models.DateTimeField()
    delivery_time = models.DateTimeField(null=True, blank=True)
    coupon = models.ForeignKey('Coupan', related_name='order_coupons', on_delete=models.SET_NULL, null=True, blank=True)
    total_after_discount = models.FloatField(null=True, blank=True)
    def __str__(self):
        return str(self.user)
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField(null=True, blank=True)
    def __str__(self):
        return str(self.order)

class Coupan(models.Model):
    code = models.CharField(max_length=20)
    discount = models.IntegerField()
    qountity = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.code


    def save(self, *args, **kwargs):
        week = datetime.timedelta(days=7)
        self.end_date = self.start_date + week
        return super(Coupan, self).save(*args, **kwargs)