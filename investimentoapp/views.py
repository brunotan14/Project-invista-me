# import render serve para renderizar a pagina htmml
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Investimento
from .forms import InvestimentoForm

#quando você quer acessar ou acessa uma página ou algum dado está sendo feita uma requisção get
#quando você envia dados através de uma página está fazendo uma requisição post

def detalhe(request, id_investimento):
     dados = {
         'dados': Investimento.objects.get(pk=id_investimento)
     }
     return render(request,'investimentos/detalhe.html',dados)
 
def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html', context=dados)


def minhapagina(request):
    info = {
        'email': 'bruno@gmail.com',
    }
    return render(request,'investimentos/minhapagina.html', info)

def criar(request):
    if request.method == 'POST':
       investimento_form = InvestimentoForm(request.POST)
       if investimento_form.is_valid():
           investimento_form.save()
       return redirect('investimentos')
    else:
       investimento_form = InvestimentoForm()
       formulario = {
            'formulario': investimento_form
            }
       return render(request,'investimentos/novo_investimento.html', context=formulario)

def editar(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    #caso a requisição seja do metodo get, ou seja, solicitando dados para serem editados 
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request,'investimentos/novo_investimento.html',{'formulario':formulario})
    # caso a requisição seja do método post, ou seja, não possui nenhum dado e será necessario envia-los
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

def excluir(request,id_investimento):
   investimento = Investimento.objects.get(pk=id_investimento)
   if request.method == "POST":
       investimento.delete()
       return redirect('investimentos')
   return render(request,'investimentos/excluir.html', {'item': investimento})