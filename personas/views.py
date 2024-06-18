from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
from django.http import JsonResponse, HttpResponse
import csv

from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
from django.http import JsonResponse, HttpResponse
import csv

def index(request):
    personas = Persona.objects.all()
    return render(request, 'persona/index.html', {'personas': personas})

def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la vista 'index'
    else:
        form = PersonaForm()

    return render(request, 'persona/index.html', {'form': form})

def obtener_datos(request):
    personas = Persona.objects.all()
    data = list(personas.values())  # Convierte los objetos QuerySet a una lista de diccionarios
    return JsonResponse(data, safe=False)

def descargar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="personas.csv"'

    writer = csv.writer(response)
    writer.writerow(['DNI / Cédula', 'Nombres', 'Apellidos', 'Sexo', 'Fecha de Nacimiento', 'Dirección', 'Teléfono', 'Correo Electrónico'])

    personas = Persona.objects.all()

    for persona in personas:
        writer.writerow([persona.dni, persona.nombres, persona.apellidos, persona.sexo, persona.fecha_nacimiento, persona.direccion, persona.telefono, persona.correo_electronico])

    return response