from django.urls import path
from .views import *

urlpatterns = [
    path('restaurant_list/', restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/', restaurant_detail, name='restaurant_detail'),
    path('order/<int:food_id>/', place_order, name='place_order'),
    path('order/success/', order_success, name='order_success'),
]

