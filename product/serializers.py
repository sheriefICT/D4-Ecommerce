from rest_framework import serializers
from .models import Product, Brand, Review
from django.db.models.aggregates import Avg




class ProductListSerializer(serializers.ModelSerializer):
    #brand = BrandListSerializer() # لعرض الداتا البراند كلها

    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    price_withTex = serializers.SerializerMethodField()

    class Meta:
        model = Product 
        fields = '__all__'

    def get_avg_rate(self, product):
        avg = product.product_reviews.aggregate(rate_avg=Avg('rate'))
        if not  avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']    

    def get_reviews_count(self, product: Product):
        reviews = product.product_reviews.all().count()
        return reviews

    def get_price_withTex(self, product):  # لعمليه حسابيه
        return product.price*5
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')

    
class ProductDetaleSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    review = ReviewSerializer(source='product_reviews', many=True)
    brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self, product):
        avg = product.product_reviews.aggregate(rate_avg=Avg('rate'))
        if not  avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']            

    def get_reviews_count(self, product: Product):
        reviews = product.product_reviews.all().count()
        return reviews




class BrandListSerializer(serializers.ModelSerializer):
      class Meta:
        model = Brand
        fields = '__all__'


class BrandDetaleSerializer(serializers.ModelSerializer):
      products = ProductListSerializer(source='product_brand' ,many=True)
      class Meta:
        model = Brand
        fields = '__all__'