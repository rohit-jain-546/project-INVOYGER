from django.urls import path 
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('products/', views.adminpd, name='adminpd'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
]
