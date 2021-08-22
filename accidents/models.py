from django.db import models

# Create your models here.
class Accident(models.Model):
    curp = models.CharField(max_length=20,blank=True)
    fecha_accidente = models.DateField(blank=False)
    residuo_fisico = models.FloatField()
    residuo_emocional = models.FloatField()
    residuo_intelectual = models.FloatField()
    residuo_intuicional = models.FloatField()

    class Meta:
        verbose_name = 'Accidente'
        verbose_name_plural = 'Accidentes'
    
    def __str__(self):
        return self.name