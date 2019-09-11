from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import *

admin.site.register(User)
admin.site.register(Environment)
admin.site.register(Board)
admin.site.register(Sensor)
admin.site.register(Data)
