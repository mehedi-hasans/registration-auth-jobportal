from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Custom_User


class UserForm(UserCreationForm):
    USER=[
        ('Applicant','Applicant'),('Recruiter','Recruiter')
        
    ]
    username=forms.CharField(label='Your Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    display_name=forms.CharField(label='Your Display Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label='Your Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    # user_type=forms.CharField(attrs={'class':'form-control'})
    user_type = forms.ChoiceField(choices=USER, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model=Custom_User
        fields=['username','display_name','email','password1','password2','user_type']


class SignInForm(forms.Form):
    username=forms.CharField(label='Your Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
  