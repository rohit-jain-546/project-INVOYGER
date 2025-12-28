from django.urls import path 
from .views import *
urlpatterns = [
    path('', user_home, name='user_home'),
    path('cart/', cart_view, name='cart'),
]
