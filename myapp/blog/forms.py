from django import forms
from django.contrib.auth.models import User 
class ContactForm(forms.Form):
    name = forms.CharField(label='name',max_length=100,required=True)
    email = forms.EmailField(label='Email',required=True)
    message = forms.CharField(label='Message',required=True)

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label='username',max_length=100,required=True) 
    email=forms.CharField(label='username',max_length=100,required=True) 
    password=forms.CharField(label='Password',max_length=100,required=True) 
    password_confirm=forms.CharField(label='password_confirm',max_length=100,required=True) 

    class Meta:
        model=User
        fields=['username','email','password']
