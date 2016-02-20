from django.db import models
from destino.models import *
from usuario.models import Usuario
from utils.countryinfo import COUNTRY_CHOICES

#ModelManager
class AerolinaManager(models.Manager):
	def queryset(self):
		return super().get_queryset().filter(is_active = True)

class MexicoCountryManager(models.Manager):
	def queryset(self):
		return super().get_queryset().filter(pais = 'MX')

# Create your models here.
class Aerolinea(models.Model):

	class Meta:
		verbose_name = "Aerolinea"
		verbose_name_plural = "Aerolineas"

	#Attributes
	nombre = models.CharField(max_length = 100, blank = False)
	pais = models.CharField(max_length = 2, choices = COUNTRY_CHOICES)
	is_active = models.BooleanField(default = True)

	#Manager
	object = AerolinaManager()
	#active = AerolinaManager()
	#mexico = MexicoCountryManager()

	def __str__(self):
		return self.nombre

class Vuelo(models.Model):

	class Meta:
		verbose_name = "Vuelo"
		verbose_name_plural = "Vuelos"

	#Relations
	aerolinea = models.ForeignKey(Aerolinea)
	destino = models.ForeignKey(Destino)

	#Attributes
	fecha = models.DateField(auto_now_add = True, blank = False)
	hora = models.TimeField(auto_now_add = True, blank = False)

	def __str__(self):
		return (self.aerolinea.nombre + " " + self.destino.nombre)

class Bitacora(models.Model):

	class Meta:
		verbose_name = "Bitacora"
		verbose_name_plural = "Bitacoras"

	#Relations
	usuario = models.ForeignKey(Usuario)
	vuelo = models.ForeignKey(Vuelo)

	def __str__(self):
		return self.usuario.usuario.first_name + " viajo a " + self.vuelo.destino.nombre