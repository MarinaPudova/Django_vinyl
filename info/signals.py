from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from info.models import InfoCollection, CollectionRecord


@receiver(m2m_changed, sender=InfoCollection.record.through)
# @receiver(m2m_changed, sender=CollectionRecord)
# def update_record_count(sender, instance, action, **kwargs):
def update_record_count(sender, instance, **kwargs):
    # if action:
    print('!!!!!!Calculate amount')
    print(instance)
    # instance.number_records = instance.records.count()
    # instance.save()


# m2m_changed.connect(update_record_count, sender=InfoCollection.record.through)
