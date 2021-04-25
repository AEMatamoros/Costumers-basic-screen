from django.urls import path
from .views import home, costumer, products, create_order, update_order, delete_order

urlpatterns = [
    path('',home ,name="home"),
    path('costumer/<str:pk>/',costumer, name="costumer" ),
    path('products/',products, name="products"),
    path('create_order/<str:pk>',create_order, name="create_order"),
    path('update_order/<str:pk>/', update_order, name="update_order"),
    path('delete/<str:pk>/', delete_order, name="delete_order"),
]