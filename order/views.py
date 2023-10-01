from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *




class OrderList(LoginRequiredMixin,ListView):
    model = Order
    paginate_py = 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset



def add_to_cart(request): # الاضافه في السله 
    qountity = request.POST['quantity'] #    استدعاء القيمه المبدئيه لعددالمنتجات من المستخدم 
    product = Product.objects.get(id=request.POST.get('product_id')) # استدعاء المنتجات  الي جايه من المستخدم 

    cart = Cart.objects.get(user=request.user, status='InPrograss') # استدعاء السله من خلال ريكوست اليوزر المفتوح 
    cart_detail, created = CartDetale.objects.get_or_create(cart=cart, product=product)# استدعاء تفاصيل السله والمنتجات الي بداخلها 

    cart_detail.quantity = int(qountity) # تحويل تفاصيل السله الي ارقام  لعمل عمليه حسابيه علي الارقام
    cart_detail.total = round( int(qountity)* product.price ,2) # حساب تقاصيل وعددهم وضربهم في سعر المنج 
    cart_detail.save() # حفظ تفاصيل السله 

    return redirect(f'/products/{product.slug}')


def remove_to_cart(request, id):
    cart_detail = CartDetale.objects.filter(id=id)
    cart_detail.delete()
    return redirect('/products/')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user, status='InPrograss')
    cart_detail= CartDetale.objects.filter(cart=cart)

    return render(request, 'order/checkout.html',{'cart_detail': cart_detail})