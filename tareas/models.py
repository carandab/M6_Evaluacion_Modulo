from django.db import models

class Tarea(models.Models):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")


    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
    

    def __str__(self):
        return self.titulo