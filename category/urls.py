from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_details, name='category_'),
    path('<slug:category_slug>/', views.category_product, name='category_product'),
    ]
