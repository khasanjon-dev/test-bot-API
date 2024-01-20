from django.contrib import admin

from .models import Science


# Register your models here.


@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('name',)
