from django import forms
from .models import OrgGroup

from itcap.settings import YEAR_CHOICES
from django.utils.dates import MONTHS


class NewGroupForm(forms.ModelForm):
    class Meta:
        model = OrgGroup
        fields = ('name', 'description')


class NewStatForm(forms.Form):
    year = forms.ChoiceField(widget=forms.Select, choices=YEAR_CHOICES.items(), initial=3)
    month = forms.ChoiceField(widget=forms.Select, choices=MONTHS.items())
    requests = forms.IntegerField()
    calls = forms.IntegerField()