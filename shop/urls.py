from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('product/<int:pk>/', views.product, name='product'),
    path('product/add_product', views.add_product, name='add_product'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
]
