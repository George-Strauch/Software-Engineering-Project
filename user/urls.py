from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name='user-profile_'),
    path('profile/', views.view_profile, name='user-profile'),
    path('register/', views.register_user, name='user-register'),
    path('sign_in/', views.sign_in, name='user-sign_in'),
]