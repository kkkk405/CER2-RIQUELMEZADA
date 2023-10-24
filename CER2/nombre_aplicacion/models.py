from django.db import models
from django.contrib.auth.models import User

class Entidad(models.Model):
    id= models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=40)
    logo= models.ImageField()#carpeta/

    def __str__(self)->str:
        return self.nombre
    
class Comunicado(models.Model):
    id= models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=55)
    detalle= models.CharField(max_length=255)
    detalle_corto= models.CharField(max_length=55)
    TIPO_CHOICES=[('S', 'Suspension de actividades'),
        ('C', 'Suspension de clases'),
        ('I','Informacion')]
    tipo= models.CharField(max_length=10, choices=TIPO_CHOICES)
    entidad= models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='entidad')
    visible= models.BooleanField(default=True)
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion= models.DateTimeField(auto_now=True)
    publicado_por= models.ForeignKey(User, on_delete=models.CASCADE, editable=False,null=True)
    modificado_por= models.ForeignKey(User, on_delete=models.CASCADE, editable=False,null=True, related_name='modificado_por')
   
    def __str__(self)->str:
        return self.titulo