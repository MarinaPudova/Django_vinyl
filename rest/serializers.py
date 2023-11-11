from rest_framework import serializers

from record.models import Record
from info.models import InfoCollection


class InfoCollectionSerializer(serializers.Serializer):
    name = serializers.CharField()
    owner = serializers.CharField()
    start_year = serializers.IntegerField()
    number_records = serializers.IntegerField()
    is_open_viewing = serializers.BooleanField()
    # record = serializers.ManyToManyField(Record, related_name="records", through="CollectionRecord")

    def create(self, validated_data):
        return InfoCollection.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.owner = validated_data.get('owner', instance.owner)
        instance. start_year = validated_data.get('start_year', instance. start_year)
        instance. number_records = validated_data.get('number_records', instance. number_records)
        instance. is_open_viewing = validated_data.get('is_open_viewing', instance. is_open_viewing)
        instance.save()
        return instance


class RecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    artist = serializers.CharField()
    realise_year = serializers.IntegerField()
    # cover = serializers.ImageField()

    def create(self, validated_data):
        return Record.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.realise_year = validated_data.get('realise_year', instance.realise_year)
        # instance.cover = validated_data.get('cover', instance.cover)
        instance.save()
        return instance
