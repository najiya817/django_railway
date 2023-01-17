from django.urls import path
from .views import HomeView

urlpatterns=[
   
    path('viewss/',HomeView.as_view())
]