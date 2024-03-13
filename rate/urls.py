from django.urls import path 
from .api import *

urlpatterns = [
    path('gatallrates/',ListAndCreateRates.as_view(),name="allRatesClassBased"),
    path('getratebyid/<int:id>',GetRateById.as_view(),name="getratebyid"),
    path('deleteratebyid/<int:id>',DeleteRateById.as_view(),name="deleteratebyid"),
    path('updateratebyid/<int:id>',UpdateRateById.as_view(),name="updateratebyid"),
]