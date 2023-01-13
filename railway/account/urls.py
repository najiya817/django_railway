from django.urls import path
from .views import log,register

urlpatterns=[
    path('login/',log),
    path('register/',register)

]