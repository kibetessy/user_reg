from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
