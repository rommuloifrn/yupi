from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    
    path('create-pin', views.CreatePinView.as_view(), name='create pin'),
]
