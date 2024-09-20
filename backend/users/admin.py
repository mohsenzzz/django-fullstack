from django.contrib import admin
from . import models
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['userName'],
    }
    list_display = ['__str__','userName', 'is_active']

admin.site.register(models.User,UserAdmin)


