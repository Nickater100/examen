from django.db import models

# Create your models here.

class Productos(models.Model):
    producto: models.CharField(max_length=100)

    def __str__(self):
        return self.producto 