from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['dni', 'nombres', 'apellidos', 'sexo', 'fecha_nacimiento', 'direccion', 'telefono', 'correo_electronico']