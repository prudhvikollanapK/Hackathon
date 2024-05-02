from django.contrib import admin
from .models import *


class VoiceToTextAdmin(admin.ModelAdmin):
    list_display = [
        'audio_data', 'language'
    ]


admin.site.register(VoiceToText, VoiceToTextAdmin)


class ImageToTextAdmin(admin.ModelAdmin):
    list_display = [
        'text'
    ]


admin.site.register(ImageToText, ImageToTextAdmin)


class PDFToTextAdmin(admin.ModelAdmin):
    list_display = [
        'text'
    ]


admin.site.register(PDFToText, PDFToTextAdmin)
