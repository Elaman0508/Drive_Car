from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import RegisterCreateView, ResetPasswordView, LoginCreateView, ChangePasswordView



urlpatterns = [
    path('register_create/', RegisterCreateView.as_view(), name='register_create'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('login/', LoginCreateView.as_view(), name='login'),


]
