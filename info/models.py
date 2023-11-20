from django.db import models

from record.models import Record


# Create your models here.


class InfoCollection(models.Model):
    """"""
    name = models.CharField(max_length=100, null=False)
    owner = models.CharField(max_length=100, null=False)
    start_year = models.PositiveSmallIntegerField()
    number_records = models.PositiveSmallIntegerField()
    # collection_cost = models.FloatField()
    is_open_viewing = models.BooleanField(default=True)

    record = models.ManyToManyField(Record, related_name="records", through="CollectionRecord")

    def __str__(self):
        return self.name


class CollectionRecord(models.Model):
    collection = models.ForeignKey(InfoCollection, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
