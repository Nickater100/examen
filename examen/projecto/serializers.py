from rest_framework import serializers
from .models import Productos
import json
from bson import ObjectId

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos  
        fields = ['id', "producto"]

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)