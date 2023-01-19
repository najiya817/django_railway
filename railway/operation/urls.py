from django.urls import path
from .views import *

urlpatterns=[
    path('add/',AddView.as_view(),name="addd"),
    path('sub/',SubView.as_view(),name="subb"),
    path('mul/',MulView.as_view(),name="mull"),
    path('div/',DivView.as_view(),name="divv"),
    path('count/',CountView.as_view(),name="strng"),

    
  
]