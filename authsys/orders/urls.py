from django.urls import path 
from .views import *
app_name='orders'
urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('order-success/<str:order_id>/', order_success, name='order_success'),
    ]
