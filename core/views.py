from django.shortcuts import render

from django.views import View

from .forms import RegisterForm

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from django import http

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')
    
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'core/register.html', {'form':form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.save()
            return http.HttpResponseRedirect('/')
        else: 
            return render(request, 'core/register', {'form':form})

class LoginView(LoginView):
    template_name = 'core/login.html'
    next_page = ''
    
class LogoutView(LogoutView):
    next_page = ''
    template_name = 'core/logout.html'