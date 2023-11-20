from django import forms

from info.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('artist', 'name', 'realise_year')
