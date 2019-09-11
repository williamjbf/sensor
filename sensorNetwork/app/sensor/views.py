from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from . import models

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

# Create your views here.


class sensores(ListView):
    model = models.Sensor
    template_name = "HTML/sensores.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = models.Board.objects.all()
        return context


class criar_sensor(CreateView):
    model = models.Sensor
    fields = ['description', 'typeDate', 'board', 'unity']
    success_url = reverse_lazy('sensores')


class Inicial(TemplateView):
    success_url = reverse_lazy('inicial')
    template_name = 'HTML/inicial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['environments'] = models.Environment.objects.all()
        context['boards'] = models.Board.objects.all()
        context['sensors'] = models.Sensor.objects.all()
        return context


class Ambientes(ListView):
    model = models.Environment
    template_name = 'HTML/ambientes.html'


class Placas(ListView):
    model = models.Board
    template_name = 'HTML/placas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['environment'] = models.Environment.objects.all()
        return context


class Criar_ambiente(CreateView):
    model = models.Environment
    fields = ['name', 'description']
    success_url = reverse_lazy('ambientes')


class Criar_placa(CreateView):
    model = models.Board
    fields = ['name', 'description','environment']
    success_url = reverse_lazy('placas')

class DataSensor(CreateView):
    model = models.Data
    fields = ['value', 'sensor']
    success_url = reverse_lazy('sensores')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(DataSensor, self).dispatch(*args, **kwargs)
