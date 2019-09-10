from django.shortcuts import render
from . import models

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class sensores(ListView):
    model = models.Sensor
    template_name = "HTML/sensores.html"
