from rest_framework import serializers

from record.models import Record
from info.models import InfoCollection


class RecordListSerializer(serializers.ModelSerializer):
    """
    show all records serializer
    """

    class Meta:
        model = Record
        fields = '__all__'


class RecordCreateSerializer(serializers.ModelSerializer):
    """
    create record serializer
    """

    class Meta:
        model = Record
        fields = '__all__'


class RecordRetrieveSerializer(serializers.ModelSerializer):
    """
    show one item of records serializer
    """

    class Meta:
        model = Record
        exclude = ('id', )


class RecordUpdateSerializer(serializers.ModelSerializer):
    """
    update record serializer
    """

    class Meta:
        model = Record
        fields = '__all__'


class InfoCollectionListSerializer(serializers.ModelSerializer):
    """
    show all collections serializer
    """
    record = serializers.SerializerMethodField()

    class Meta:
        model = InfoCollection
        fields = ('id', 'name', 'owner', 'start_year', 'number_records', 'record')

    def get_record(self, obj):
        """
        show full information about records in selected collection
        :param obj: current collection
        :return: all records in current collection
        """
        records = obj.record.all()
        return (record.full_record_name for record in records)


class InfoCollectionCreateSerializer(serializers.ModelSerializer):
    """
    create collection serializer
    """
    record = serializers.PrimaryKeyRelatedField(
        many=True, allow_empty=False, queryset=Record.objects.all().order_by('artist', 'name', )
    )

    class Meta:
        model = InfoCollection
        fields = ('name', 'owner', 'start_year', 'record')


class InfoCollectionRetrieveSerializer(serializers.ModelSerializer):
    """
    show one item of collections serializer
    """
    record = serializers.SerializerMethodField()

    class Meta:
        model = InfoCollection
        fields = ('name', 'owner', 'start_year', 'number_records', 'record')

    def get_record(self, obj):
        """
        show full information about records in selected collection
        :param obj: current collection
        :return: all records in current collection
        """
        records = obj.record.all()
        return (record.full_record_name for record in records)


class InfoCollectionUpdateSerializer(serializers.ModelSerializer):
    """
    update collection serializer
    """
    record = serializers.PrimaryKeyRelatedField(
        many=True, allow_empty=False, queryset=Record.objects.all().order_by('artist', 'name', 'realise_year',)
    )

    class Meta:
        model = InfoCollection
        fields = ('name', 'owner', 'start_year', 'number_records', 'record')


class InfoCollectionDestroySerializer(serializers.ModelSerializer):
    """
    delete collection serializer
    """

    class Meta:
        model = InfoCollection
