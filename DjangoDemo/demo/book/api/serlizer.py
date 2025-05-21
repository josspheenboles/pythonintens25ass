from ..models import *
from rest_framework import serializers

class CatagorySerlizer(serializers.ModelSerializer):
    class Meta:
        model =Catagory2
        fields='__all__'

