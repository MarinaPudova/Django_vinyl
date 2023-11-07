from datetime import datetime

from django.contrib import admin
from django.utils.html import format_html

from info.admin import CollectionRecordInline
from info.models import CollectionRecord
from record.models import Record


# Register your models here.


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_cover', 'artist', 'name', 'realise_year', 'new_item')
    readonly_fields = ('display_cover', 'new_item')
    # readonly_fields = ('new_item',)
    list_filter = ('artist', 'realise_year')
    search_fields = ('artist', 'name')
    ordering = ('artist', '-realise_year')
    # list_editable = ('realise_year',)

    fieldsets = (
        ('Description of record', {
            'fields': ('artist', 'name', 'realise_year', 'new_item', 'display_cover'),
        }),
        ('Photo of cover', {
            'fields': ('cover',),
            'classes': ('collapse',)
        })
    )

    def new_item(self, obj):
        return "new" if obj.realise_year == datetime.now().year else "---"


    def display_cover(self, obj):
        return format_html('<img src="{}" height="50"/>', obj.cover.url) if obj.cover else "No cover"

    display_cover.short_description = 'Cover'
