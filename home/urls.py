from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/' , views.login, name = 'login'),
    path('register/' , views.register, name = 'register'),
    path('faculty/<str:username>' , views.faculty, name = 'faculty'),
    path('security/<str:username>' , views.security, name = 'security'),
    path('visitor/<str:username>' , views.visitor, name = 'visitor'),
    path('visitor/<str:username>/<int:fid>' , views.visitormail, name = 'visitormail'),
    path('accept/<str:tokenid>',views.accept, name = 'accept'),
    path('decline/<str:tokenid>',views.decline, name = 'decline')
]
