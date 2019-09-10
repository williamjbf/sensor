from django.shortcuts import render
from .models import *

# Create your views here.
class sensores(DetailView):
    model = model.Sensor
    template_name = "template/sensores.html"
