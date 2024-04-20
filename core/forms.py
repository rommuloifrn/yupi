from django import forms
from .models import Pin

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['url', 'text', 'visible']