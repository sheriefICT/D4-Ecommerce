from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Brand, ProductImages, Review
from django.db.models import Q , F, Value
from django.db.models.aggregates import Sum, Min, Max, Avg, Count




# def QuerySet_Debug(request):
#     #data = Product.objects.all() # عرض جميع الداتا بالطريقه العادية
#     #data = Product.objects.select_related('brand').all() # عرض الداتا في عالاه علاقات وان تو وان -- وا وان تو مني 
#     #data = Product.objects.filter(price__gt = 70) # فلتر اكبر من
#     #data = Product.objects.filter(price__gte = 50) #   فلتر اكبر من او يساوى
#     #data = Product.objects.filter(price__lt = 30) #   فلتر اقل من 
#     #data = Product.objects.filter(price__lte = 70) #   فلتر اقل من او يساوى 
#     #data = Product.objects.filter(price__range = (70, 80)) #   فلتر ما بين رينجين قيمتين
#     #data = Product.objects.filter(brand__name = 'Apple') #  navgate relations فلتر  لقيمه علافه
#     #data = Product.objects.filter(brand__price__gt=35) # 
#     #data = Product.objects.filter(name__contains = 'Brown') # فلتر تيكست
#     #data = Product.objects.filter(name__startswith = 'e') #  فلتر تيكست يبدا بقيمه محدده
#     #data = Product.objects.filter(name__endswith = 'l') #   فلتر تيكست ينتهي بقيمه محدده
#     #data = Product.objects.filter(tags__isnull= True) #   فلتر للقيمه الفارغه
#     #data = Review.objects.filter(created_at__year= 2023 ) #   فلتر للتاريخ بالسنه
#     #data = Review.objects.filter(created_at__month__range= (8, 9) ) #   فلتر للتاريخ بالشهر وقيمه من والي 
#     #data = Product.objects.filter(price__gt= 80, quantity__lt=10 ) #   فلتر لقيمتين مع بعض
#     # data = Product.objects.filter(
#     #     Q(price__gt=80 ) |
#     #     Q(quantity__lt=10)                                                 
#     # ) # فلتر لقيمتين منفصلتين

#     # data = Product.objects.filter(
#     #     Q(price__gt=80 ) &
#     #     Q(quantity__lt=10)                                                 
#     # ) # فلتر لقيمتين مع بعض

#     # data = Product.objects.filter(
#     #     Q(price__gt=80 ) &
#     #     ~Q(quantity__lt=30)                                                 
#     # ) # فلتر لعكس القيمه ض
#     #data = Product.objects.filter(price=F('quantity')) # فلتر لمقارنه قيمتين ض
#     #data = Product.objects.all().order_by('name') # فلتر بالاسم اسندينح
#     #data = Product.objects.order_by('name') # فلتر بالاسم اسندينح
#     #data = Product.objects.order_by('-name') # فلتر بالاسم ديسندينح
#     #data = Product.objects.order_by('name').reverse # فلتر بالاسم ديسندينح
#     #data = Product.objects.order_by('name','quantity') # فلتر  بعمودين
#     #data = Product.objects.order_by('name','quantity').reverse # فلتر  بعمودين
#     #data = Product.objects.order_by('name')[0] # فلتر  اول قيمه
#     #data = Product.objects.order_by('name')[-1] # فلتر  اخر قيمه
#     #data = Product.objects.earliest('name') # فلتر  اول قيمه
#     #data = Product.objects.latest('name') # فلتر  اخر قيمه

#     #data = Product.objects.all()[10:] # فلتر  تحديد قيمه
#     #data = Product.objects.values('name', 'price') # فلتر  تحديده عمود
#     #data = Product.objects.values('name', 'price', 'brand__name') # فلتر  تحديد وعلاقه
#     #data = Product.objects.values_list('name', 'price', 'brand__name') #  فلتر  تحديد وعلاقه داخل ليست
#     #data = Product.objects.all().distinct()#  فلتر  بدوت تكرار 
#     #data = Product.objects.only('name', 'price')#   فلتر  تحديد اعمده مع مراعاه العلاقات
#     #data = Product.objects.defer('slug', 'dsecreiption')#  فلتر تحديد جميع اعمده ما عدا اعمده معينه
#     #data = Product.objects.aggregate(Sum('quantity'))#  جمع عمود
#     #data = Product.objects.aggregate(Avg('price'))#  جمع عمود
#     #data = Product.objects.annotate(price_with_tex =F('price')*5)#  عمليات حسابيه علي العمود


 

    
#     return render(request,'product/QuerySet.html',{'data': data})

class ProductList(ListView):
    model = Product
    paginate_by = 20


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_product"] = Product.objects.filter(brand=self.get_object().brand)
        return context 
    
class BrandList(ListView):
    model = Brand   
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))

class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    paginate_by = 20


    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context



