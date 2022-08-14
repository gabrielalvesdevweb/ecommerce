from django.views.generic.list import ListView
from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models


class ProductList(ListView):
    template_name = 'productList.html'

class ProductDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DETALHE DO PRODUTO')

class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('ADICIONAR NO CARRINHO')

class RemoveToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('REMOVER DO CARRINHO')

class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('CARRINHO')

class Search(View):
    def get(self, *args, **kwargs):
        return HttpResponse('BUSCA')

class Pay(View):
    def get(self, *args, **kwargs):
        return HttpResponse('PAGAMENTO')

class SaveOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse('SALVAR PEDIDO')

class OrderList(View):
    def get(self, *args, **kwargs):
        return HttpResponse('LISTA DE PEDIDOS')

class OrderDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DETALHE DO PEDIDO')
