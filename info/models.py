from django.db import models

# Create your models here.


class InfoCollection(models.Model):
    """"""

    name = models.CharField(max_length=100, null=False)
    owner = models.CharField(max_length=100, null=False)
    start_year = models.PositiveSmallIntegerField()
    number_records = models.PositiveSmallIntegerField()
    collection_cost = models.FloatField()
