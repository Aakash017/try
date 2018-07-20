from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomTrainee


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomTrainee
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomTrainee
        fields = ('username', 'email')