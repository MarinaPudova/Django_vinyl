from django_filters import rest_framework as django_filters

from info.models import InfoCollection
from record.models import Record


class RecordFilter(django_filters.FilterSet):
    """
    All filters for records
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    realise_year = django_filters.RangeFilter()
    artist = django_filters.ModelChoiceFilter(
        queryset=Record.objects.values_list('artist', flat=True).distinct(),
        field_name='artist',
        to_field_name='artist',
        lookup_expr='exact',
        label='Artists',
    )
    name_and_artist = django_filters.CharFilter(
        method='filter_by_name_and_artist',
        label="Part name of record, part name of artists, eg 't,ram'",
    )

    class Meta:
        model = Record
        fields = ('name', 'realise_year', 'artist', )

    def filter_by_name_and_artist(self, queryset, name, value):
        parts = value.split(',')
        name_record = parts[0]
        name_artist = parts[1]
        if name_record:
            queryset = queryset.filter(name__icontains=name_record)
        if name_artist:
            queryset = queryset.filter(artist__icontains=name_artist)
        return queryset


class InfoCollectionFilter(django_filters.FilterSet):
    """
    All filters for collections
    """
    owner = django_filters.CharFilter(lookup_expr='icontains')
    start_year = django_filters.RangeFilter()
    number_records = django_filters.NumberFilter()
    record = django_filters.ModelChoiceFilter(
        queryset=Record.objects.all(),
        field_name='record',
        to_field_name='id',
        lookup_expr='exact',
        label='Records',
    )

    class Meta:
        model = InfoCollection
        fields = ('owner', 'start_year', 'number_records', 'record', )
