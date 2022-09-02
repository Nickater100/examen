from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Productos

class Serializador(ModelSerializer):
    class Meta:
        model = Productos
        fields=["id", "producto"]