from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsuarioSerializer
from .models import Usuario

@api_view(['POST'])
def criar_usuario(req):
    dados = req.data
    usuario = Usuario.objects.create_user(
        username=dados['username'], 
        password=dados['password'], 
        telefone=dados['telefone']
        )

    return Response({'Usuário criado'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(req):
    dados = req.data
    usuario = authenticate(username=dados['username'], password=dados['password'])
    
    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            }, status=status.HTTP_200_OK
        )
    else:
        return Response({'Erro:': 'Usuario ou senha inválidos'}, status=status.HTTP_400_BAD_REQUEST)