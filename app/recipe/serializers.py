"""
Recipe app serializers.
"""
from rest_framework import serializers
from core import models


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe Model"""

    class Meta:
        model = models.Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for single recipe instance"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = models.Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
