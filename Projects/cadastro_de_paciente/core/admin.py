from django.contrib import admin

# Register your models here.
from .models import Patient, Insurance

admin.site.register(Patient)
admin.site.register(Insurance)