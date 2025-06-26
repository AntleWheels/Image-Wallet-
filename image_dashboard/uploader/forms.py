from django import forms
from django.contrib.auth.models import User
from .models import ImageUpload

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    mobile = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'password']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']