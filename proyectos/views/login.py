#Users views

# Django REST FRAMEWORK
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#serializer
from proyectos.serializers.login import *
from proyectos.serializers.user import *

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        
        #Hadlle HTTP POST    request.
        serializer =  UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
