from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import UsuarioForm

class Cadastro(View):
    template_name = 'cadastro.html'
    form_class = UsuarioForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    