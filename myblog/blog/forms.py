from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Choose category'

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'rows': 10}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
            'is_published': forms.CheckboxInput(attrs={'class': "form-check-input", 'type': 'checkbox',
                                                       'label': 'is_published'}),
            'cat': forms.Select(attrs={'class': "form-select form-select-sm"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Length of title more than 200 symbols')

        return title


# watch widgets and read django documentation about widgets
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'first name'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'last name'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'username'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'you@example.com'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='repeat the password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-control rounded-3',
                                                                            'placeholder': 'username'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3',
                                                                                   'placeholder': 'password'}))
