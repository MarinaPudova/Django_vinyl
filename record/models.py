from django.db import models

# Create your models here.


class Record(models.Model):
    """"""
    name = models.CharField(max_length=100, null=False)
    artist = models.CharField(max_length=100, null=False)
    realise_year = models.PositiveSmallIntegerField()

    # info_collection = models.ForeignKey(
    #     InfoCollection, on_delete=models.CASCADE, related_name='collection_id', default=None
    # )


    def __str__(self):
        return f'{self.artist} {self.name}'






