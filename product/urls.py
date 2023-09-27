from django.urls import path , include
from .views import * 
from .api import *

urlpatterns = [
    path('', ProductList.as_view()),
    # path('QuerySet', QuerySet_Debug),
    path('<slug:slug>', ProductDetail.as_view()),
    path('brand/', BrandList.as_view()),
    path('brand/<slug:slug>', BrandDetail.as_view()),



 
    #api as function
    # path('api/list', product_list_api),
    # path('api/list/<int:product_id>', product_detale_api),

    
   #api as class genarecs
    path('api/list', ProductLisAPI.as_view()),
    path('api/list/<int:pk>', ProductDetaleAPI.as_view()),
    path('brand/api/list', BrandListAPI.as_view()),
    path('brand/api/list/<int:pk>', BrandDetaleAPI.as_view()),

]