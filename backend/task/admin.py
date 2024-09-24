from django.contrib import admin
from . import models
# Register your models here.

class taskAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title','created_at']

admin.site.register(models.Task,taskAdmin)