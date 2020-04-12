from rest_framework import serializers
from .models import FavoriteBook
class FavoriteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=FavoriteBook
        fields='__all__'
