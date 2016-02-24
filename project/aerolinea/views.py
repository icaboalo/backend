from django.shortcuts import render
from .models import *

# Create your views here.
def vuelos(request):

	vuelo = Vuelo.object.all()
	vuelos = {}
	
	for x in vuelo:
		aerolinea = x.aerolinea.nombre
		destino = x.destino.nombre
		vuelos.setdefault(aerolinea, []).append(destino)

	return render(request, 'vuelos.html', {'vuelos' : vuelos})

	