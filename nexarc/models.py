from django.db import models


class VoiceToText(models.Model):
    audio_data = models.CharField(max_length=2000)
    language = models.CharField(max_length=2000, default="")

    def __str__(self):
        return f"Audio Data: {self.audio_data}, Language: {self.language}"



class ImageToText(models.Model):
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.text

class PDFToText(models.Model):
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.text
