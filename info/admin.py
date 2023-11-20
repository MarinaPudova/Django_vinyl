from django.contrib import admin

from info.models import InfoCollection, CollectionRecord


# admin.site.register(InfoCollection)
# Register your models here.


@admin.register(InfoCollection)
class InfoCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'start_year', 'number_records')
    list_filter = ('name',)
    search_fields = ('start_year', 'number_records',)
    # sortable_by = ('collection_cost',)


@admin.register(CollectionRecord)
class CollectionRecord(admin.ModelAdmin):
    list_display = ('id', 'collection', 'record')
