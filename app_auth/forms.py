from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, PasswordInput, CharField, EmailInput

class UserRegisterForm(UserCreationForm):
    password1 = CharField(label='', widget=PasswordInput(
        attrs={
            'class': 'input is-success', 'placeholder': 'Password'}
        ))
    password2 = CharField(label='', widget=PasswordInput(
        attrs={
            'class': 'input is-success', 'placeholder': 'Confirm Password'}
        ))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password1', 'password2')

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'input is-success',
                'placeholder': 'First Name'
            }),
            'email': EmailInput(attrs={
                'class': 'input is-success',
                'placeholder': 'Email'
            }),
            'username': TextInput(attrs={
                'class': 'input is-success',
                'placeholder': 'Username'
            }),

        }

class UserLoginForm(AuthenticationForm):
    username = CharField(label='', widget=PasswordInput(
        attrs={
            'class': 'input is-success', 'placeholder': 'Username'}
        ))
    password = CharField(label='', widget=PasswordInput(
        attrs={
            'class': 'input is-success', 'placeholder': 'Password'}
        ))
    class Meta:
        model = User
        fields = ('username', 'password')