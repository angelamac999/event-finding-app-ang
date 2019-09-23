from django.forms import ModelForm
from .models import Event, Category

class EventForm(ModelForm):

    class Meta:

        model = Event
        fields = ['title', 'location', 'venue', 'start_time', 'end_time']






# from django.contrib.auth.models import User
# from django import forms
# from .models import Event
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column


# class NewEventForm(forms.ModelForm):

#     class Meta:
#         model = Event
#         fields = ['title', 'location', 'venue', 'start_time', 'end_time']


# class AccountForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']   




# import datetime
# from django import forms
# from django.forms import ModelForm
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
# from .models import Event, Category
# from django.shortcuts import render

         # def clean_event_date(self):

    #     data = self.cleaned_data['start_time']        
    #     # Check if a date is not in the past.
    #     if data < datetime.date.today():
    #         raise ValidationError(_('Invalid date - event is in past'))
    #         # Check if a date is in the allowed range (+4 weeks from today).
    #     if data > datetime.date.today() + datetime.timedelta(weeks=52):
    #         raise ValidationError(_('Invalid date - renewal more than 1 year ahead'))
    #         # Remember to always return the cleaned data.
    #     return data