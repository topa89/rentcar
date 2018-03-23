from django import forms

class SubscriberForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
             'class': 'form-control',
             'placeholder': 'Email',
             'id': 'emailinput',
             }
    ))