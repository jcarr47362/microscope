from django import forms
from django_my_user.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = MyUser
        fields = ["displayname"]



