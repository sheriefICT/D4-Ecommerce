from django_filters import rest_framework as  filter
from .models import Product


class ProductFilter(filter.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['contains'],
            'price': ['range', 'lte','gte'],
        }
