from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from .models import *

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'text', 'item']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']