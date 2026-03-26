from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import UsuarioForm

class Cadastro(View):
    template_name = 'cadastro.html'
    form_class = UsuarioForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Usuário cadastrado com sucesso!')
        return render(request, self.template_name, {'form': form})