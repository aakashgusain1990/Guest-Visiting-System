"""GVI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from log import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name = 'welcome'),
    path('login',views.login,name = 'login'),
    path('signin',views.signin,name = 'signin'),
    path('visitorsignin',views.visitorsignin,name = 'visitorsignin'),
    path('facultysignin',views.facultysignin,name = 'facultysignin'),
    path('securitysignin',views.securitysignin,name = 'securitysignin'),
    path('securitypage',views.securitypage,name = 'securitypage'),
    path('visitorpage',views.visitorpage,name = 'visitorpage'),
    path('facultypage',views.facultypage,name = 'facultypage'),
    path('makeapp',views.makeapp,name = 'makeapp'),
    path('viewappvisitor',views.viewappvisitor,name = 'viewappvisitor'),
    path('secview',views.secview,name = 'secview'),
    path('visitor/random/<int:fid>', views.random, name = 'random'),
]
