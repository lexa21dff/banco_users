from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.proyecto import *


class ProyectoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put