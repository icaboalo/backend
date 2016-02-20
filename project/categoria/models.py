from django.db import models

#ModelManager
class Aventurero(models.Manager):
	def queryset(self):
		return super().get_queryset().filter(categoria = Aventurero)

# Create your models here.
class Categoria(models.Model):

	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"

	#Attributes
	categoria = models.CharField(max_length = 100, blank = False)

	def __str__(self):
		return self.categoria