# from django.db.models.signals import post_save, m2m_changed
# from django.dispatch import receiver
#
# from info.models import InfoCollection, CollectionRecord
#
#
# # @receiver(m2m_changed, sender=InfoCollection.record.through)
# @receiver(m2m_changed, sender=CollectionRecord)
# def record_save(sender, instance, action, **kwargs):
#     if action == 'post_add':
#         print('!!!!!!Uiiiiiii. Calculate amount')
#         # instance.save()
