from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('joinEvent/', views.joinEvent, name='joinEvent'),
    path('leaveEvent/', views.leaveEvent, name='leaveEvent'),
]