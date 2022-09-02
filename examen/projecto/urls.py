from django.urls import path
from . import views

urlpatterns = [
 path("", views.home, name="home"),
 path("agregar/", views.agregar, name="agregar"),
 path("eliminar/<int:id>/", views.eliminar, name="eliminar"),
 path("editar/<int:id>/", views.editar, name="editar"),
]