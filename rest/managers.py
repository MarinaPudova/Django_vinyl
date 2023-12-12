from django.db import models


class CollectionManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_open_viewing=True)


class ClosedCollectionManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_open_viewing=False)
