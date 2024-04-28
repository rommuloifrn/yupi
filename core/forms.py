from django import forms
from .models import Pin, User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class PinForm(forms.Form):
    video_id = forms.CharField(max_length=200)
    text = forms.CharField(max_length=200, widget=forms.Textarea)
    visible = forms.BooleanField(required=False)

class EditPinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['text', 'visible']
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'location']