from django.urls import path
from .views import LogView,RegisterView

urlpatterns=[
    path('login/',LogView.as_view()),
    path('register/',RegisterView.as_view())

]