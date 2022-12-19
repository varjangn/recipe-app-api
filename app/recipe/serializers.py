"""
Recipe app serializers.
"""
from rest_framework import serializers
from core import models


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = models.Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe Model"""
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = models.Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link', 'tags']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create recipe with tags"""
        tags = validated_data.pop('tags', [])
        recipe = models.Recipe.objects.create(**validated_data)

        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = models.Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)

        return recipe

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for single recipe instance"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
