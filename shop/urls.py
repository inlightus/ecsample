from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('drafts/', views.product_draft_list, name='product_draft_list'),
    path('product/<pk>/publish/', views.product_publish, name='product_publish'),
    path('product/<pk>/remove/', views.product_remove, name='product_remove'),
]
