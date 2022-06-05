from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image', 'bio',)
        exclude=('user','password1','password2')

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')