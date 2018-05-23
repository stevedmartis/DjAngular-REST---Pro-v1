from django.contrib import admin
from .models import Modulo
# Register your models here.



class ModuloAdmin(admin.ModelAdmin):
    # list_display = ["id",  "nombre", "porcent", "estado", ]
    # list_editable     = [ "nombre", "porcent", "estado",  ]
    # list_filter	       = [  "nombre" , "estado", ]
    filter_horizontal = [ "usuario", ]

    # search_fields = ["nombre"]
    class Meta:
        model = Modulo
        

admin.site.register(Modulo, ModuloAdmin)
