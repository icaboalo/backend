from django.db import models
from django.contrib.auth.models import User
from categoria.models import *

# Create your models here.
class Usuario(models.Model):

	class Meta:
		verbose_name = "Usuario"
		verbose_name_plural = "Usuarios"

	#Relations
	usuario = models.ForeignKey(User)
	perfil = models.ForeignKey(Categoria)

	#Attributes
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return (self.usuario.first_name + " " + self.usuario.last_name)