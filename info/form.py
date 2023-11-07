from django import forms

from info.models import InfoCollection, CollectionRecord
from record.models import Record


class InfoCollectionForm(forms.ModelForm):
    class Meta:
        model = InfoCollection
        fields = ('name', 'owner', 'start_year', 'number_records', 'records')

    records = forms.ModelMultipleChoiceField(
        queryset=Record.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class CollectionRecordForm(forms.ModelForm):
    class Meta:
        model = CollectionRecord
        fields = ('collection', 'record')
