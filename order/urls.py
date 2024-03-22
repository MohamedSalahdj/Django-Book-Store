from django.urls import path
from .views import *


urlpatterns = [
    # path('orders/add-order/', add_order,name='add_order'), 
    path('orders/publisher/<int:publisher_id>/', get_publisher_orders, name='get_publisher_orders'), 
    path('orders/customer/<int:customer_id>/', get_customer_orders, name='get_customer_orders'), 
    path('orders/<int:id>/Update/', update_order, name='update_order'), 
    path('orders/<int:id>/delete/', delete_order, name='delete_order'), 
    
    path('<int:id>/orders/create', CreateOrderAPI.as_view()),
    path('<int:id>/cart', CartDetailCreateAPI.as_view()),
    

]