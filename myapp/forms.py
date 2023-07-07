from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import MobileStore

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class MobilePhoneForm(forms.ModelForm):
    class Meta:
        model=MobileStore
        fields=["name","model","rate","storage","pic","description","user"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "rate":forms.TextInput(attrs={"class":"form-control"}),
            "storage":forms.TextInput(attrs={"class":"form-control"}),
            "pic":forms.FileInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            

        }