from django import forms
from django.core.exceptions import ValidationError
from users.models import User

class LoginForm(forms.Form):
    userId = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder": "전화번호, 사용자 이름 또는 이메일"}
        )
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호"},
        ),
    )
class SignupForm(forms.Form):
    userId = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "휴대폰 번호 또는 이메일 주소"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "성명"}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "사용자 이름"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"}))

    def cleam_userId(self):
        userId = self.cleaned_data["nickname"]
        if User.objects.filter(userId=userId).exists():
            raise ValidationError(f"입력한 사용자명 {{userId}}은 이미 사용 중입니다.")
        return userId

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 4:
            self.add_error("password", "비밀번호는 4자리 이상이어야 합니다.")

    def save(self):
        userId = self.cleaned_data["userId"]
        password = self.cleaned_data["password"]
        nickname = self.cleaned_data["nickname"]
        name = self.cleaned_data["name"]
        user = User.objects.create_user(
            userId=userId,
            password=password,
            username=nickname,
            name=name,
        )
        return user