"""
Recipe app serializers.
"""
from rest_framework import serializers
from core import models


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe Model"""
    class Meta:
        model = models.Recipe
        fields = ['id', 'title', 'time_minute', 'price', 'link']
        read_only_fields = ['id']
