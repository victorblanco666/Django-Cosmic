from django.db import models

# Create your models here.

    
class Usuario(models.Model):
    id_usuario  = models.AutoField(db_column='idUsuario', primary_key=True) 
    usuario    = models.CharField(max_length=20)
    contraseña  = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id_usuario)