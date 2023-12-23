from django import forms
from django.core import validators


class ContactMeForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=50)
    last_name = forms.CharField(min_length=1, max_length=50)
    phone_number = forms.CharField()
    e_mail = forms.EmailField(validators=[validators.EmailValidator])
    message = forms.Textarea()
