from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['username', 'email', 'password1', 'password2']  # Include the fields you want


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['birthday', 'profile_picture']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }