from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('singup/', views.singup_user, name='singup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
