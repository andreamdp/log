# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class log(models.Model):
    fecha = models.DateField(auto_now=True)
    tipo=models.CharField(max_length=50,'Tipo de Rebote')
    email=models.CharField(max_length=70)
    

