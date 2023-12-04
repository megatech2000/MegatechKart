
from . import  views
from django.urls import path


urlpatterns = [
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('user_logout', views.user_logout, name='user_logout'),


]