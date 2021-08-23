from django.urls import path
from . import views

urlpatterns = [
    path('boxapp/', views.CustomerList.as_view()),
]