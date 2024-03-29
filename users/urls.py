from django.urls import path
from .views import CreateUser, GetUsers, GetUser, UpdateUser, DeleteUser, CreatePublisher,ChangeUserPassword, ListPublisherAPI

urlpatterns = [
    path('', GetUsers.as_view(), name='user-list'),
    path('create/', CreateUser.as_view(), name='user-create'),
    path('<int:pk>/', GetUser.as_view(), name='user-detail'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='user-update'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='user-delete'),
    path('<int:pk>/change-password/', ChangeUserPassword.as_view()),

    # publisher 
    path('create-publisher/', CreatePublisher.as_view(), name='create_publisher'),
    path('publisher-list/', ListPublisherAPI.as_view()),

]
