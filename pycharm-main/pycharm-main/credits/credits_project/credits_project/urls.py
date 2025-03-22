"""
URL configuration for credits_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path

from app import views

urlpatterns = [
    # path('', views.general, name='general'),
    path('admin/', views.admin, name='admin'),
    path('general/', views.general, name='general'),
    path('login/', views.login, name='login'),
    path('my_applications/', views.my_applications, name='my_applications'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.login, name = 'logout'),
]