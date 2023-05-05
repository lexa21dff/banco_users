from rest_framework import serializers
from proyectos.models import Inscrito

class Equipo_trabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inscrito
        fields = ['url', 'id','codigo_grupo']
