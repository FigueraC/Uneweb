from django.db import models

class Persona(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    dni = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'