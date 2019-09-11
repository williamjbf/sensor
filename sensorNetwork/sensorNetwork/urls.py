"""sensorNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.sensor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicial.as_view(), name='inicial'),
    path('sensores/', views.sensores.as_view(), name='sensores'),
    path('criar_sensor/', views.criar_sensor.as_view(), name='criar_sensor'),
    path('ambientes/', views.Ambientes.as_view(), name ='ambientes'),
    path('placas/', views.Placas.as_view(), name='placas'),
    path('criar_placa',views.Criar_placa.as_view(), name='criar_placa'),
    path('criar_ambiente',views.Criar_ambiente.as_view(), name='criar_ambiente'),
    path('datasensor/', views.DataSensor.as_view(), name='send_data'),
]
