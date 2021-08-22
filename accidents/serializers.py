from rest_framework import serializers
from .models import Accident

class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = ('id','curp','fecha_accidente','residuo_fisico','residuo_emocional','residuo_intelectual','residuo_intuicional') 