from django import forms
from .models import Pin, User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['video_id', 'text', 'visible']

class EditPinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['text', 'visible']
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'location']