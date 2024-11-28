from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['username', 'email', 'password1', 'password2']  # Include the fields you want
