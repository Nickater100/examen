from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProdForm
from pymongo import MongoClient

client = MongoClient("localhost")

db = client["Examen"]

# Create your views here.

def home(request):
    productos = Productos.objects.all()
    context = {"productos":productos}
    return render (request, "projecto/home.html", context)

    

def agregar(request):
     col = db["tabla"]
     col.insert_one({
                "action":"agregar", 
                "producto":"arroz", 
                "Query":"insert into"
            })
     if request.method == "POST":
         form = ProdForm(request.POST)
         col.insert_one({
                "action":"agregar", 
                "producto":"form", 
                "Query":"insert into"
            })
         if form.is_valid(): 
             form.save()

             return redirect("home")
     else:
         form = ProdForm()

     context = {'form': form}
     return render(request, "projecto/agregar.html", context)



def eliminar(request, id):
    col = db["tabla"]
    producto = Productos.objects.get(id=id)
    col.insert_one({
                "action":"delete", 
                "producto":Productos.objects.get(id=id), 
                "Query":"delete from"
            }) 
    producto.delete()
    return redirect("home")

def editar(request, id):
    col = db["tabla"]
    producto = Productos.objects.get(id=id)
    print(producto)
    if col.count_documents({}) > 10:
        col.delete_one({}) 
    if request.method == "POST":
        form = ProdForm(request.POST, instance=producto)
        if(form.is_valid()):
            form.save()
            return redirect("home")
    else:
        form = ProdForm(instance=producto)

    context = {"form" :form}
    return render(request, "projecto/editar.html", context)


    