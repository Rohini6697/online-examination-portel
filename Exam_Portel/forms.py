from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    # role = forms.ChoiceField(choices=Profile.ROLL_CHOICES)

    class Meta:
        model = User
        fields = ['username','email','password']
        help_texts = {
            'username' : None
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password does not match')
        return cleaned_data
    

class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)