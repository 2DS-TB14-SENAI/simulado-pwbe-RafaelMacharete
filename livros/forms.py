from django import forms
from .models import Livro

class LivroForm(forms.Form):
    class Meta:
        model = Livro
        fields = '__all__'