from rest_framework import serializers
from .models import User
from .models import Types
from .models import Menu
from .models import Basket

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class TypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Types 
        fields= '__all__'


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'

class BasketSerializers(serializers.ModelSerializer):
    class Meta:
        model=Basket
        fields='__all__'

