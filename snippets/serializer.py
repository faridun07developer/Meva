from rest_framework import serializers
from snippets.models import Fruits


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = '__all__'
