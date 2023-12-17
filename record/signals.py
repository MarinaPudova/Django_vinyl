# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from info.models import InfoCollection
# from record.models import Record
#
#
# @receiver(post_save, sender=Record)
# def record_save(sender, instance, created, **kwargs):
#     if created:
#         print('Record save. Calculate amount')
#         # recalculate_record_collection()
#
#
# # def recalculate_record_collection(instance_collection: InfoCollection):
# #     records = instance_collection.source_collection.
