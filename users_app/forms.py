from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CustomRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    #roll_no=forms.NumberInput()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
