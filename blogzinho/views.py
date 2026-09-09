from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your views here.

def meu_blog(request):
    return HttpResponse('mensagem da url <blog>!!!!!!')
def teste_foda(request):
    return HttpResponse('testei aqui essa porraaaaaaaaaaaaaaaaaaa')