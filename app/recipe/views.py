"""View for recipe APIs"""

from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core import models
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.RecipeDetailSerializer
    queryset = models.Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Manage Tag in the DB"""
    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated users"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
