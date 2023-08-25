from django.urls import path
from . views import *

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', DetailView.as_view()),

]