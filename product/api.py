from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .myfilter import ProductFilter
from .mypagination import MyPagination



from .serializers import *
from .models import Product, Brand


###################### start API As Functions #######################
# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:5]
#     data = ProductSerializer(products, many=True, context={'request': request}).data
#     return Response({'products': data})


# @api_view(['GET'])
# def product_detale_api(request, product_id):
#     products = Product.objects.get(id=product_id)
#     data = ProductSerializer(products,context={'request': request}).data
#     return Response({'product': data}) 
###################### End API As Functions #######################

###################### start API As Class genarecs #######################

# class ProductLisAPI(generics.ListAPIView):  # للعرض قفط
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductLisAPI(generics.ListCreateAPIView):  #  Rest-FrameworkAPIللعرض والاضافه مع النظر الي ديكومنتاشن مكتبه 
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    #filterset_fields = ['flag', 'brand']
    #search_fields = ['name', 'subtitle', 'dsecreiption']
    #ordering_fields = ['price', 'quantity'] #  ,والنظر ال المكتبه'__all__'كما يمكن الفلتر 
    filterset_class = ProductFilter
    pagination_class = MyPagination
    

class ProductDetaleAPI(generics.RetrieveUpdateDestroyAPIView):  #  Rest-FrameworkAPIللعرض والاضافه مع النظر الي ديكومنتاشن مكتبه 
    queryset = Product.objects.all()
    serializer_class = ProductDetaleSerializer


class BrandListAPI(generics.ListCreateAPIView): 
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

class BrandDetaleAPI(generics.RetrieveAPIView): 
    queryset = Brand.objects.all()
    serializer_class = BrandDetaleSerializer