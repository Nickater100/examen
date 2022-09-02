from django import forms
from .models import Productos

class ProdForm(forms.ModelForm):

     class Meta:
         model = Productos
         fields =['producto']
