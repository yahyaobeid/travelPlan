from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password', 'confirm_password']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic', 'name', 'email', 'username', 'bio', 'location']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

        return user