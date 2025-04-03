from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import LivroSerializer
from .models import Livro

@api_view(['GET'])
def listar_livros(req):
    todos_livros = Livro.objects.all()
    return render(req, 'livros.html', {'todos_livros': todos_livros})

@api_view(['POST'])
def criar_listar_livros(req):
    if req.method == 'POST':
        livro_serializer = LivroSerializer(data=req.data)
        if livro_serializer.is_valid():
            livro_serializer.save()
            return Response(livro_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(livro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'GET':
        todos_livros = Livro.objects.all()
        todos_livros_serializer = LivroSerializer(todos_livros)
        return Response(livro_serializer.data, status=status.HTTP_200_OK)