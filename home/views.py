from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def minha_home(request):
    return HttpResponse('home!')

def meu_blog(request):
    return HttpResponse('mensagem da url <blog>!')