from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProdForm

# Create your views here.

def home(request):
    productos = Productos.objects.all()
    context = {"productos":productos}
    return render (request, "todo/home.html", context)

def agregar(request):
    if request.method == "POST":
        form = ProdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProdForm()

    context = {'form': form}
    return render(request, "projecto/agregar.html", context)