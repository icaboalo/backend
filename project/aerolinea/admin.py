from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Aerolinea)
admin.site.register(models.Vuelo)
admin.site.register(models.Bitacora)