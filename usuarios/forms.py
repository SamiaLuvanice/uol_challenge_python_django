from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone','grupo']
        widgets = {
            'grupo': forms.RadioSelect(attrs={'class': 'teste'})
        }

        