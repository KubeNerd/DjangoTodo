from django.contrib import admin
from .models import TaskBd

# Register your models here.
                           #Estou usando um decorator
admin.site.register(TaskBd)# ou @admin.register(TaskBd)

class TaskAdmin(admin.ModelAdmin):
    lista_display=('id','conteudo','data',)