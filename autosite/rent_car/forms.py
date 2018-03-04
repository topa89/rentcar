from django import forms
from django.core.exceptions import ValidationError

class OrderForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    lease_term = forms.IntegerField()

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 1:
            raise ValidationError('Имя слишком короткое')
        return name    