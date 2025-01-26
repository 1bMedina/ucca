from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from .models import Stoves
from django.forms import ModelForm, ChoiceField


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class StovesSearch(ModelForm):
    print("work")
    class Meta:
        model = Stoves
        fields = ['experience', 'climate', 'stove_location', 'use']
        widgets = {
            'experience': ChoiceField(),
            'climate': ChoiceField(),
            'stove_location': ChoiceField(),
            'use': ChoiceField(),
        }

