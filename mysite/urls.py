"""mysite URL Configuration

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
from django.urls import include, path

from django.views.generic import TemplateView, ListView, DetailView

urlpatterns = [
    path('',TemplateView.as_view(template_name="QuickTutor/index.html")),
    path('login/',TemplateView.as_view(template_name="login/loginPage.html")),
    path('aboutus/',TemplateView.as_view(template_name="QuickTutor/aboutus.html")),
    path('profile/',TemplateView.as_view(template_name="QuickTutor/profile.html")),
    path('admin/', admin.site.urls),
    path('QuickTutor/', include('QuickTutor.urls')),
    path('accounts/', include('allauth.urls')),
]
