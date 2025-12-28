from django.urls import path 
from .views import *
urlpatterns = [
    path('', user_home, name='user_home'),
]
