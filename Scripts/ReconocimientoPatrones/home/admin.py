from django.contrib import admin

from .models import Tejido
from .models import Paciente

# Register your models here.

class TejidoAdmin(admin.ModelAdmin):
    list_display = ("color", "temperatura", "inflammation", "name")
    list_filter = ("color",)
    #readonly_fields = ("color",)
    ordering = ("color",)
    search_fields = ("color",)

admin.site.register(Tejido, TejidoAdmin)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Paciente, PacienteAdmin)