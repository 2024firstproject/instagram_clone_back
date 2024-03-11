from django import forms

class LoginForm(forms.Form):
    userId = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder": "전화번호, 사용자 이름 또는 이메일"},
        ),
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호"},
        ),
    )