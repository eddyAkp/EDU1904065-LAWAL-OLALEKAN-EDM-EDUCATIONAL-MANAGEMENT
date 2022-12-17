from django.contrib import admin

from resources.models import (Author,
                              InformationMaterial,
                              AudioVisualMaterial,
                              PrintMediaMaterial,
                              SerialPrintMediaMaterial,
                              )

# Register your models here.

BASE_LIST_DISPLAY = ['title', 'author', 'quantity', 'price_per_unit']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(InformationMaterial)
class InformationMaterialAdmin(admin.ModelAdmin):
    list_display = BASE_LIST_DISPLAY


@admin.register(AudioVisualMaterial)
class AudioVisualMaterialAdmin(admin.ModelAdmin): pass


@admin.register(PrintMediaMaterial)
class PrintMediaMaterialAdmin(admin.ModelAdmin):
    list_display = BASE_LIST_DISPLAY[:2] + ['ISBN'] + BASE_LIST_DISPLAY[2:] + ['publish_date']


@admin.register(SerialPrintMediaMaterial)
class SerialPrintMediaMaterialAdmin(admin.ModelAdmin):
    list_display = BASE_LIST_DISPLAY[:1] + ['serialization_display'] + BASE_LIST_DISPLAY[1:]
