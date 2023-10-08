from django import forms


class SoftappForm(forms.ModelForm):
    number = forms.IntegerField()