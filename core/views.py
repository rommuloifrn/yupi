from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django import http
from django.shortcuts import get_object_or_404
from django.views import View
from .services import PinService

from .forms import RegisterForm, PinForm, EditProfileForm, EditPinForm

from .models import Pin, User

from abc import abstractclassmethod
from .youtube_api_bridge import APIHandler, Parser


@method_decorator(login_required, name='dispatch')
class LoginRequiredView(View):
    @abstractclassmethod
    def get():
        pass
    def post():
        pass
    
    
class HomeView(View):
    def get(self, request):
        pins = Pin.objects.all()
        return render(request, 'core/home.html', {'pins':pins})
    
class ProfileView(LoginRequiredView):
    def get(self, request):
        return render(request, 'core/user/profile.html', {'user':request.user})
    
            
class EditProfileView(LoginRequiredView):
    def get(self, request):
        data = {'bio':request.user.bio, 'location':request.user.location}
        form = EditProfileForm(instance=request.user)
        return render(request, 'core/user/edit_profile.html', {'form':form})
    def post(self, request):
        user = request.user
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user.bio = form.cleaned_data['bio']
            user.location = form.cleaned_data['location']
            user.save()
            return http.HttpResponseRedirect('/profile')
        else:
            return render(request, '')
    
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'core/auth/register.html', {'form':form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.save()
            return http.HttpResponseRedirect('/')
        else: 
            return render(request, 'core/auth/register', {'form':form})

class LoginView(LoginView):
    template_name = 'core/auth/login.html'
    next_page = '/'
    
class LogoutView(LogoutView):
    next_page = ''
    template_name = 'core/auth/logout.html'
    
class SearchUserView(View):
    def post(self, request):
        query = request.POST.get('usernamequery', '')
        users = User.objects.filter(username__icontains=query)
        return render(request, 'core/user/search.html', {'users':users})

class ReadUserView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        return render(request, 'core/user/another_profile.html', {'user':user})
        

class CreatePinView(LoginRequiredView):
    def get(self, request):
        form = PinForm()
        return render(request, 'core/crud/pin/create.html', {'form':form})
    def post(self, request):
        form = PinForm(request.POST)
        if form.is_valid():
            new_pin = Pin(user=request.user, text=form.cleaned_data['text'], visible=form.cleaned_data['visible'])
            PinService.create_pin(request, new_pin, form.cleaned_data['video_id'])
            return http.HttpResponseRedirect('/')
        else: 
            return render(request, 'core/crud/pin/create.html', {'form':form})
        
class UpdatePinView(LoginRequiredView):
    def get(self, request, *args, **kwargs):
        pin = get_object_or_404(Pin, pk=kwargs['pk'])
        form = EditPinForm(instance=pin)
        return render(request, 'core/crud/pin/update.html', {'form':form, 'pin':pin})
    def post(self, request, *args, **kwargs):
        form = EditPinForm(request.POST)
        if form.is_valid():
            pin = get_object_or_404(Pin, pk=kwargs['pk'])
            pin.text = form.cleaned_data['text']
            pin.visible = form.cleaned_data['visible']
            pin.save()
            return http.HttpResponseRedirect('/profile')
        else:
            return render(request, 'core/crud/pin/update.html', {'form':form, 'pin':pin})
        
class DeletePinView(LoginRequiredView):
    def post(self, request, *args, **kwargs):
        pin = get_object_or_404(Pin, id=kwargs['pk'])
        pin.delete()
        return http.HttpResponseRedirect('/profile')
    
class ReadPinView(View):
    def get(self, request, *args, **kwargs):
        pin = get_object_or_404(Pin, id=kwargs['pk'])
        videoinfo = APIHandler.get_video_info(pin.video_id)
        
        return render(request, 'core/crud/pin/read.html', {'pin':pin, 'videoinfo':videoinfo})
        