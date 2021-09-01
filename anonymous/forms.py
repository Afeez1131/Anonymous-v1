from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
