from rest_framework import serializers
from .models import PGLlist

class PgllistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGLlist
        fields = '__all__'