from django.db import models

# Create your models here.

class Rol(models.Model):
    tiporol=models.CharField(max_length=45)
    class Meta:
        
        db_table= "rol"

class Usuario(models.Model):
    nombre =models.CharField(max_length=50)
    contrasenia= models.CharField(max_length=15)
    idrol =models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    class Meta:
        db_table="usuario"

class Empleado(models.Model):  
    nombre =models.CharField(max_length=45)  
    genero= models.CharField(max_length=45)
    edad =models.IntegerField()
    telefono=models.CharField(max_length=45)
    cargo=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    direccion=models.CharField(max_length=45)
    usuarioid=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    class Meta:
        db_table= "empleado"

