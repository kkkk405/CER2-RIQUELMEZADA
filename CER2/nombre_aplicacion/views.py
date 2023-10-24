from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad

def index(request):
    titulo="Inicio"

    if request.GET.get("entidad") =='todos' or request.GET.get("entidad") is None:
        comunicados = Comunicado.objects.all()

    else:
        entidad_a_filtrar = Entidad.objects.get(nombre=request.GET.get("entidad"))
        comunicados = Comunicado.objects.filter(entidad=entidad_a_filtrar)
        
    data ={
        'titulo': titulo,
        'comunicados_totales': comunicados.count(),
        'comunicados': comunicados.order_by('-fecha_publicacion'),
        'entidades_totales': Entidad.objects.count(),
        'entidades': Entidad.objects.all(),
        'entidad_eleguida': request.GET.get("entidad")
    }
    return render(request, 'nombre_aplicacion/index.html', data)

