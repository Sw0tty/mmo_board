"""
URL configuration for mmo_board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import PasswordChangeView

from account.views import ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('advertisements/', include('board.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', ProfileView.as_view()),
    path('accounts/profile/password_change/', PasswordChangeView.as_view(
        template_name='change-password.html',
        success_url='/accounts/profile/'
    ), name='password_change'),
]
