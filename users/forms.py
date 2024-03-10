from django import forms

class LoginForm(forms.Form):
    userId = forms.CharField(min_length=3)
    password = forms.CharField(min_length=4)