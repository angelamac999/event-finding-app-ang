from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from django.forms import ModelForm



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

    # def save(self, commit=True)
    #     user = super(CustomUserCreationForm, self).save(commit=False)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
                 'email',
                 'first_name',
                 'last_name'
                )


# class EditProfileForm(ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = (
#                  'email',
#                  'first_name',
#                  'last_name'
#                 )

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column