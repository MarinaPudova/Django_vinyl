from django.db import models

# Create your models here.


class Record(models.Model):
    """"""
    name = models.CharField(max_length=100, null=False)
    artist = models.CharField(max_length=100, null=False)
    realise_year = models.PositiveSmallIntegerField()
    cover = models.ImageField(upload_to='records/', blank=True, null=True)

    @property
    def full_record_name(self):
        return f"{self.artist} '{self.name}', {self.realise_year}"

    def __str__(self):
        return self.full_record_name






