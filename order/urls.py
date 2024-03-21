from django.urls import path
from . import views


urlpatterns = [
    path('orders/add-order/', views.add_order,name='add_order'), 
    path('orders/', views.get_orders,name='get_orders'), 
    path('orders/<int:id>/', views.get_order,name='get_order'), 
    path('orders/<int:id>/update/', views.update_order,name='update_order'), 
    path('orders/<int:id>/delete/', views.delete_order,name='delete_order'), 
  

]