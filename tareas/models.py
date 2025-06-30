from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
