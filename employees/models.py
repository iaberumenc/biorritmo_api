from django.db import models

# Create your models here.
class Employee(models.Model):
    curp = models.CharField(max_length=20,blank=True)
    fecha_nacimiento = models.DateField(blank=False)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
        constraints = [
                models.UniqueConstraint(fields=['curp'], name='')
            ]
    
    def __str__(self):
        return self.name