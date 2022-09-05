from rest_framework import serializers
from .models import Productos

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos  
        fields = ['id', "producto"]

class MongoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos  
        fields = ['_id',"action", "producto", "Query"]