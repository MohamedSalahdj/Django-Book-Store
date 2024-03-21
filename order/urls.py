from django.urls import path
from .views import *


urlpatterns = [
<<<<<<< HEAD
    path('orders/add-order/', views.add_order,name='add_order'), 
    path('orders/', views.get_orders,name='get_orders'), 
    path('orders/<int:id>/', views.get_order,name='get_order'), 
    path('orders/<int:id>/update/', views.update_order,name='update_order'), 
    path('orders/<int:id>/delete/', views.delete_order,name='delete_order'), 
  
=======
    path('orders/add-order/', add_order,name='add_order'), 
    path('orders/', get_orders,name='get_orders'), 
    path('orders/<int:id>/', get_order,name='get_order'), 
    path('orders/<int:id>/Update/', update_order,name='update_order'), 
    path('orders/<int:id>/delete/', delete_order,name='delete_order'), 


    path('<int:id>/cart', CartDetailCreateAPI.as_view()),

>>>>>>> main

]