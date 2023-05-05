



#Django
from django.contrib.auth import authenticate
#django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserLoginSerializer(serializers.Serializer):
    #User login serializer
    #Handle the  login request data
    #email = serializers.EmailField()
    username = serializers.CharField(min_length=4,max_length=20)
    password = serializers.CharField(min_length=8,max_length=64)

    def validate(self,  data):
        #verificar credenciales
        user = authenticate(username=data['username'], password=data['password'])
        #user = authenticate(username=data['email'],password=data['password'])
        #user = authenticate(request=request, email=email, password=password)
        
        print(user)
        if not user:
            raise serializers.ValidationError('invalido las credenciales')

        #limitar login a usurios con cuenta verificada
        # if not user.is_verified:
        #     raise serializer.ValidationError('cuenta no verificada')
        self.context['user']=user
        return data
    
    def create (self,data):
        #Genetate or retrieve new token
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

        
        

# class UserLoginSerializer(serializers.Serializer):
#     #User login serializer
#     #Handle the  login request data
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=8,max_length=64)

#     def validate(self, data):
#         #verificar credenciales
#         user = authenticate(username=data['email'],password=data['password'])
#         print(user)
#         if not user:
#             raise serializers.ValidationError('invalido las credenciales')
#         self.context['user']=user
#         return data
    
#     def create (self,data):
#         #Genetate or retrieve new token
#         token, created = Token.objects.get_or_create(user=self.context['user'])
#         return self.context['user'], token.key
