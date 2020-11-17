from django import forms

class emailForm(forms.Form):
    subject = forms.CharField(label='Name of Entity', max_length=100)
    message = forms.CharField(label='Description   ', max_length=500)