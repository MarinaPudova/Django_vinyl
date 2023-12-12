from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from info.models import InfoCollection, CollectionRecord


# admin.site.register(InfoCollection)
# Register your models here.

class CollectionRecordInline(admin.TabularInline):
    model = CollectionRecord
    extra = 5


@admin.register(InfoCollection)
class InfoCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'start_year', 'number_records', 'display_records', 'is_open_viewing')
    list_filter = ('owner', 'name',)
    search_fields = ('start_year', 'number_records',)
    ordering = ('owner', 'name',)
    # list_editable = ('is_open_viewing',)

    actions = ('open_viewing', 'close_viewing')
    inlines = (CollectionRecordInline,)

    def display_records(self, obj):
        records = obj.record.all()
        href = '<a href="{}">{}</a>'
        url = 'admin:record_record_change'
        links = [format_html(href, reverse(url, args=[rec.id]), f'{rec.artist} "{rec.name}"') for rec in records]
        return format_html(', '.join(links))
        # return ', '.join([f'{rec.artist} "{rec.name}"' for rec in obj.record.all()])

    def open_viewing(self,request, queryset):
        queryset.update(is_open_viewing=True)
        self.message_user(request, 'Selected collections have been opened for viewing')

    def close_viewing(self, request, queryset):
        queryset.update(is_open_viewing=False)
        self.message_user(request, 'Selected collections have been closed for viewing')

    display_records.short_description = 'Records'
    open_viewing.short_description = 'Open collections for viewing'
    close_viewing.short_description = 'Close collections for viewing'


@admin.register(CollectionRecord)
class CollectionRecord(admin.ModelAdmin):
    list_display = ('id', 'collection', 'record')
