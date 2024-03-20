from django.urls import path 
from .api import *

urlpatterns = [
    path('get-all-rates/<int:id>',allBookRates,name="allRatesClassBased"),
    path('get-rate/<int:id>',GetRateById.as_view(),name="get-rate"),
    path('create-rate/',CreateRates.as_view(),name="create-rate"),
    path('delete-rate/<int:id>',DeleteRateById.as_view(),name="delete-rate"),
    path('update-rate/<int:id>',UpdateRateById.as_view(),name="update-rate"),
]