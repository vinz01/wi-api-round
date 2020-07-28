from django import forms
from .models import user, manager
class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', max_length=20)
    class Meta:
        model = user
        fields = ("username", "password")

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     #user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user

class PasswordForm(forms.Form):
    userid = forms.CharField(label='username', max_length=20)
    webusername = forms.CharField(label='webusername', max_length=20)
    webpwd = forms.CharField(label='webpwd', max_length=20)
    website = forms.CharField(label='website', max_length=20)
    class Meta:
        model = manager
        fields = ("userid", "webusername", "webpwd", "website")

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', max_length=20)