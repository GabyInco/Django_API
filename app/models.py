from django.db import models

# Create your models here.
class Usuario(models.Model):
    
   Nombre = models.CharField(max_length=150)
   Apellido = models.CharField(max_length=150)
   Usuario = models.CharField(max_length=10)
   Clave = models.CharField(max_length=50)
   Correo = models.CharField(max_length=150)
   # BANNER = models.ImageField(upload_to='imagenes/', null=True,verbose_name='algo')
   # En caso que necesitemos subur una imagen  nuestra base de datos