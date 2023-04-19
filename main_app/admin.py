from django.contrib import admin
from .models import Psychologist, Patient, Consulta, Record

# Register your models here.
admin.site.register(Psychologist)
admin.site.register(Patient)
admin.site.register(Consulta)
admin.site.register(Record)