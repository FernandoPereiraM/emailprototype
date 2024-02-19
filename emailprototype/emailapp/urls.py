from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserAPI.as_view()),
    path('user/<int:pk>/', views.UserDetailsAPI.as_view()),
]


