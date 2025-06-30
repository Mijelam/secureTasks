from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
    
