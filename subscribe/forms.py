from django import forms

from subscribe.models import Subscription
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'
        # labels = {
        #     'first_name': _('enter your First Name')
        # }
        error_messages = {
            'first_name': {
                'required': _('First name is Must')
            }
        }


# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Invalid Name, must not include commas')
#     return value


# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=200, validators=[validate_comma])
#     last_name = forms.CharField(max_length=200, validators=[validate_comma])
#     email = forms.EmailField(max_length=200)
