from rest_framework import serializers
from .models import Hot 
from .models import Cold
from .models import Snacks
from .models import Dessert

class HotDSerializers(serializers.ModelSerializer):
    class Meta:
        model=Hot 
        fields=['id', 'name', 'description']

class ColdDSerializers(serializers.ModelSerializer):
    class Meta:
        model=Cold 
        fields= '__all__'


class DessertSerializers(serializers.ModelSerializer):
    class Meta:
        model=Dessert
        fields=['id', 'name', 'description']

class SnacksSerializers(serializers.ModelSerializer):
    class Meta:
        model=Snacks
        fields=['id', 'name', 'description']

