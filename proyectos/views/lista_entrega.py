from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.contrib.auth.models import User 
from proyectos.models import Entrega, Proyecto,Inscrito, Perfil
from proyectos.views.funciones import *



# @login_required
@require_GET
def entregas_por_usuario_proyecto(request, user_id, proyecto_id):
    
    perfil_inscrito = perfil_conectado(user_id) #objeto 
    entregas_por_usuario = Entrega.objects.filter(aprendiz=perfil_inscrito, )[:10]  # limitamos a 10 entregas
    
    inscrito = Inscrito.objects.filter(perfil = perfil_inscrito) #lista
    

    user = get_object_or_404(Inscrito, id=user_id)
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    entregas = Entrega.objects.filter(aprendiz=user_inscrito, proyecto=proyecto)[:10]  # limitamos a 10 entregas

    data = {
        'entregas': list(entregas.values())
    }

    return JsonResponse(data)
