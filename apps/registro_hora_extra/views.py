from .models import RegistroHoraExtra
#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
#, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.views import View


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)