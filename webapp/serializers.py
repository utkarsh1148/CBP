from rest_framework import serializers
from . models import CCDatails


class CCSerializer(serializers.ModelSerializer):
    class Meta:
        model=CCDatails
        fields='__all__'