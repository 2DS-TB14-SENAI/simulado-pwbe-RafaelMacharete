from .models import UsuarioAbs
from rest_framework import serializers

class UsuarioAbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAbs
        fields = ['username', 'password', 'telefone']