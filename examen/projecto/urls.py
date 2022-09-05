from django.urls import path
from .views import *
app_name = 'api'
urlpatterns = [
    path('productos', Post_APIView.as_view()), 
    path('productos/<int:pk>/', Post_APIView_Detail.as_view()),   
    path('mongo', Post_Mongo.as_view()),   
]