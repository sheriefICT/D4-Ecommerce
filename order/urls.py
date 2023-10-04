from django.urls import path
from .views import * 
from .api import *


app_name = 'order'

urlpatterns = [
    path('', OrderList.as_view()),
    path('checkout', checkout),
    path('add-to-cart', add_to_cart, name='add_to_cart'),
    path('<int:id>/remove-to-cart', remove_to_cart, name='remove_to_cart'),
# api
    path('api/<str:username>/cart', CartDetailCreateAPI.as_view()),

]
