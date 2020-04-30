"""SE_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as uv
from rentals import views as rv

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rv.home, name='rentals-home'),
    path('property/<prop_pk>', rv.view_property, name='prop-detail'),
    path('create_property/', rv.create_property, name='prop-create'),
    path('create_reservation/<prop_pk>', rv.rent_property, name='res-create'),
    path('register/', uv.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='rentals/home.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
