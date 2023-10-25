from django import forms

from info.models import InfoCollection


class InfoCollectionForm(forms.ModelForm):
    class Meta:
        model = InfoCollection
        fields = ('name', 'owner', 'start_year', 'number_records', 'collection_cost')
