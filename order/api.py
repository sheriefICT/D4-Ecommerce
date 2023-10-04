from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .serializers import *
from .models import *
from product.models import Product


class CartDetailCreateAPI(generics.GenericAPIView):
    serializer_class = CartSerializer
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart,created = Cart.objects.get_or_create(user=user, status='InPrograss')
        data = CartSerializer(cart).data
        return Response({'cart': data})