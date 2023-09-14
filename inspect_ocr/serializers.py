from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        
    def get_result(self, obj):
        return obj.result
    
    
    def create(self, validated_data):
        return Image.objects.create(**validated_data)