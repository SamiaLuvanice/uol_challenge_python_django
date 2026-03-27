from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import UsuarioForm
import requests

class Cadastro(View):
    template_name = 'cadastro.html'
    form_class = UsuarioForm

    def get(self, request):
        codinome = self._get_codinome('V')
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            codinome = self._get_codinome(form.cleaned_data['grupo'])
            obj = form.save()
            return HttpResponse('Usuário cadastrado com sucesso!')
           
        return render(request, self.template_name, {'form': form})
    
    def _get_codinome(self, grupo):
        if grupo =='V':
            response  = requests.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/vingadores.json').json()
            codinomes = [i['codinome'] for i in response['vingadores']]
            print(codinomes)
        elif grupo == 'LJ':
            ...
