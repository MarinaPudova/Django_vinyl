from django.contrib import admin

from record.models import Record


# Register your models here.

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist', 'realise_year')


