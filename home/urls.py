#urls.py
from django.contrib import admin  
from django.urls import path  
from home import views  
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index),
    path('login/',views.login),
    path('home/',views.home),
]  