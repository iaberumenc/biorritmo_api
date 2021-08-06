from django.db import models

# Create your models here.
class Accident(models.Model):
    curp = models.CharField(max_length=20,blank=True)
    fecha_accidente = models.DateField(blank=False)
    resoduo_fisico = models.FloatField()
    resoduo_emocional = models.FloatField()
    resoduo_intelectual = models.FloatField()
    resoduo_intuicional = models.FloatField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
        constraints = [
                models.UniqueConstraint(fields=['rfc'], name='')
            ]

    def __str__(self):
        return self.name