from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import *

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    food_items = restaurant.foods.all()
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'food_items': food_items})

@login_required
def place_order(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    order = Order.objects.create(user=request.user, restaurant=food.restaurant, total_price=food.price)
    return redirect('order_success')

def order_success(request):
    return render(request, 'order_success.html')