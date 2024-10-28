# accounts/forms.py

from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.EmailField(help_text='Must be a Harvard or Yale email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not (email.endswith('@college.harvard.edu') or email.endswith('@yale.edu')):
            raise forms.ValidationError('Please use a Harvard or Yale email address.')
        return email
