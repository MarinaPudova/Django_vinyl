from django.db.models.signals import post_save
from django.dispatch import receiver

from record.models import Record


@receiver(post_save, sender=Record)
def record_save(sender, instance, created, **kwargs):
    if created:
        print(f'Record {instance.name} save.')
