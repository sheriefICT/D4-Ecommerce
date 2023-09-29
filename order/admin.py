from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartDetale)
admin.site.register(Coupan)