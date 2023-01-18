from django.urls import path
from .views import LogView,RegisterView


urlpatterns=[
    path('login/',LogView.as_view(),name="log"),
    path('register/',RegisterView.as_view(),name="reg")
    

]