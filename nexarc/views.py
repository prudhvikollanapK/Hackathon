from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from nexarc.models import *
import pytesseract
from PIL import Image as PILImage
import fitz

from nexarc.serializers import VoiceToTextSerializer


def index_view(request):
    return render(request, 'nexarcIndex.html')


def voice_to_text_view(request):
    return render(request, 'voiceConventor.html')


def image_to_text_view(request):
    return render(request, 'imageConventor.html')


def pdf_to_text_view(request):
    return render(request, 'pdfConventor.html')


@csrf_exempt
def voice_to_text(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        audio_data = data.get('audio_data')
        language = data.get('selectedLanguage')
        print('Received audio data in language:', language)
        voice_to_text_data = VoiceToText(
            audio_data=audio_data,
            language=language
        )
        voice_to_text_data.save()
        data = {'message': 'Audio data received and saved successfully', 'data': audio_data}
        return JsonResponse(data, safe=False)

    else:
        return JsonResponse({'error': 'Invalid request method'})



@api_view(['GET'])
def fetch_texts(request):
    texts = VoiceToText.objects.all().order_by('-id')
    serialized_texts = VoiceToTextSerializer(texts, many=True).data
    data = {'message': 'Texts fetched successfully', 'data': serialized_texts}
    return JsonResponse(data, safe=False)



@csrf_exempt
def image_to_text(request):
    if request.method == 'POST':
        image_data = request.FILES.get('image_data')
        if image_data:
            image = PILImage.open(image_data)
            text = pytesseract.image_to_string(image)
            image_to_text_data = ImageToText(
                text=text
            )
            image_to_text_data.save()
            return JsonResponse({'text': text})
        else:
            return JsonResponse({'error': 'No image data provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def pdf_to_text(request):
    if request.method == 'POST':
        pdf_data = request.FILES.get('pdf_data')
        if pdf_data:
            text = ""
            with fitz.open(stream=pdf_data.read(), filetype="pdf") as pdf:
                for page in pdf:
                    text += page.get_text()
            pdf_to_text_data = PDFToText(
                text=text
            )
            pdf_to_text_data.save()
            return JsonResponse({'text': text})
        else:
            return JsonResponse({'error': 'No PDF data provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


