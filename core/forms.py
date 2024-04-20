from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    