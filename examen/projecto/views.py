from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MongoSerializers, PostSerializers
from .models import Productos
from rest_framework import status
from django.http import Http404
from pymongo import MongoClient
import json 
client = MongoClient("localhost", port=27017)

db = client["Examen"]

col = db["info"]
    
class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Productos.objects.all()
        serializer = PostSerializers(post, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            col.insert_one({"action":"post", 
                "producto":serializer.data["producto"], 
                "Query":"insert into"})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Post_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)  
        col.insert_one({"action":"get", 
                "producto":serializer.data["producto"], 
                "Query":"select from"})
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            col.insert_one({"action":"update", 
                "producto":serializer.data["producto"], 
                "Query":"update table"})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)
        col.insert_one({"action":"delete", 
                "producto":serializer.data["producto"], 
                "Query":"delete from "})
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Post_Mongo(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = col.find({})
        return Response(json.dumps(list(post)))
        