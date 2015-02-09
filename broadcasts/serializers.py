from rest_framework import serializers
from broadcasts.models import Slide, Broadcasting, Channel

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('file', 'broadcasting', 'dt_create')
        
class SlideGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('file', 'broadcasting', 'position', 'dt_upload')