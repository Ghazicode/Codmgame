from django.contrib import admin
from . import models




@admin.register(models.Services)
class serviceAdmin(admin.ModelAdmin):
    list_display = ('title', )