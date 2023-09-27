from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Product, Brand
from rest_framework import generics

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



class ProductDetaleAPI(generics.RetrieveUpdateDestroyAPIView):  #  Rest-FrameworkAPIللعرض والاضافه مع النظر الي ديكومنتاشن مكتبه 
    queryset = Product.objects.all()
    serializer_class = ProductDetaleSerializer


class BrandListAPI(generics.ListCreateAPIView): 
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

class BrandDetaleAPI(generics.RetrieveAPIView): 
    queryset = Brand.objects.all()
    serializer_class = BrandDetaleSerializer