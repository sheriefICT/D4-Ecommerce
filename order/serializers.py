from rest_framework import *
from rest_framework import serializers
from .models import *
from django.db.models.aggregates import *
from product.serializers import *


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetale
        fields = '__all__'
class CartSerializer(serializers.ModelSerializer):
    cart_detale = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'        