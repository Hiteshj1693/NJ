from django import forms
from django.forms import fields
from .models import SignupMaster

class SignupForm(forms.ModelForm):
    class Meta:
        model=SignupMaster
        fields='__all__'