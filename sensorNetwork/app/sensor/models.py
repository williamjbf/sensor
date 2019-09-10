from django.conf import settings
from django.urls import reverse

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Permission, User

class User(AbstractUser):

    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Enviroment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.CharField(max_length=200, default= '', verbose_name='Descrição', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'


class Board(models.Model):
    name = models.CharField(max_length=30, verbose_name='Placa')
    description = models.CharField(max_length=250, default= '', verbose_name='Descrição', blank=True)
    enviroment = models.ForeignKey(Enviroment, on_delete=models.PROTECT,null=True, blank=True, related_name='boards')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Placa'
        verbose_name_plural = 'Placas'


class Sensor(models.Model):
    description = models.CharField(max_length=255, default= '', verbose_name='Descrição', blank=True)
    typeDate = models.CharField(max_length=100, verbose_name='Tipo',blank=True)
    unity = models.CharField(max_length=10, verbose_name='Unidade',blank=True)
    board = models.ForeignKey(Board, on_delete=models.PROTECT, null=True, blank=True, related_name='sensor')
    
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'


class Data(models.Model):
    value = models.CharField(max_length=100,default='',verbose_name='Valor')
    date = models.DateField(max_length=100, verbose_name='Data',null=True, auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, blank=True, related_name='data')

    class Meta:
        verbose_name = 'Dado do Sensor'
        verbose_name_plural = 'Dados do Sensor'
