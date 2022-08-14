from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models

class SingUp(View):
    def get(self,*args, **kwargs):
        return HttpResponse('CADASTRAR')

class Login(View):
    def get(self,*args, **kwargs):
        return HttpResponse('LOGIN')

class Logout(View):
    def get(self,*args, **kwargs):
        return HttpResponse('Logout')

class Update(View):
    def get(self,*args, **kwargs):
        return HttpResponse('ATUALIZAR')



