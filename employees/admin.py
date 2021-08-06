from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','curp','rfc','fecha_nacimiento','fecha_accidente']
    search_fields = ['curp','rfc']