from django.db import models
from categoria.models import *
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.countryinfo import COUNTRY_CHOICES

#ModelManager
class RatingManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(rating_gt = 2)

class MexicoCountryManager(models.Manager):
	def get_queryset(self):
		return super(MexicoCountryManager, self).get_queryset().filter(pais = 'MX')

# Create your models here.
class Destino(models.Model):

	class Meta:
		verbose_name = "Destino"
		verbose_name_plural = "Destinos"

	#Relations
	categoria = models.ForeignKey(Categoria)

	#Attributes
	nombre = models.CharField(max_length = 100, blank = False)
	pais = models.CharField(choices = COUNTRY_CHOICES, max_length = 2, blank = False)
	Continente = models.CharField(max_length = 100, blank = False)
	imagen = models.ImageField(upload_to = 'media/pais/', blank = True)
	is_active = models.BooleanField(default = True)
	rating = models.IntegerField(blank = True, validators = [MaxValueValidator(10),
            MinValueValidator(1)])

	#Manager
	object = models.Manager()
	top10 = RatingManager()
	mexico = MexicoCountryManager()

	def __str__(self):
		return (self.pais + " " + self.nombre)
