from django import forms
from .models import Memory
from django.contrib.auth import get_user_model

User = get_user_model()

class MemoryForm(forms.ModelForm):
    shared_with = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Share with"
    )

    class Meta:
        model = Memory
        fields = ['title', 'description', 'memory_type', 'media_file','shared_with']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a short description...'}),
        }