from django.urls import path 
from .views import *

urlpatterns = [
   path("", user_home, name="user_home"),
    path("adminp/", admin_home, name="admin_home"),
    path('signup/', signup, name='signup'),
    path('login/', login_p, name='login'),
    path('logout/', logout_p, name='logout'),
    path('adminpd/', adminpd, name='adminpd'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
]