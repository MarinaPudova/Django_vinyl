from django.contrib import admin

from authentication.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'first_name', 'last_name', 'username', 'birth_date', 'email',
                    'phone_number', 'country', 'city')
