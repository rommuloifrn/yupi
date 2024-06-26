from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.EditProfileView.as_view(), name='edit profile'),
    path('search-user', views.SearchUserView.as_view(), name='search user'),
    path('read-user/<int:pk>', views.ReadUserView.as_view(), name='read user'),
    
    path('create-pin', views.CreatePinView.as_view(), name='create pin'),
    path('read-pin/<int:pk>', views.ReadPinView.as_view(), name='read pin'),
    path('update-pin/<int:pk>', views.UpdatePinView.as_view(), name='update pin'),
    path('delete-pin/<int:pk>', views.DeletePinView.as_view(), name='delete pin')
]
