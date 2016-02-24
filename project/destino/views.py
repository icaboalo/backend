from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	d = Destino.mexico.all()
	return render(request, 'index.html', {'destino' : d})