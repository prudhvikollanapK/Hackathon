from rest_framework import serializers
from nexarc.models import VoiceToText


class VoiceToTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceToText
        fields = '__all__'