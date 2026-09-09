# first commit

from django.db import models
from django.shortcuts import render
from django.urls import path


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.lista.html", {"produtos": produtos})
