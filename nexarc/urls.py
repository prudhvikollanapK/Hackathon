from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from nexarc.views import *

urlpatterns = [
    path('', index_view, name='index_view'),
    path('voice-to-text/', voice_to_text_view, name='voice_to_text_view'),
    path('image-to-text/', image_to_text_view, name='image_to_text_view'),
    path('pdf-to-text/', pdf_to_text_view, name='pdf_to_text_view'),
    path('voiceToText/', voice_to_text, name='voice_to_text'),
    path('imageToText/', image_to_text, name='image_to_text'),
    path('pdfToText/', pdf_to_text, name='pdf_to_text'),
    path('fetchText/', fetch_texts, name='fetch_texts'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
