# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import csv
def handle(self, *args, **options):
    with open('test.csv') as f:
     reader = csv.reader(f)
     for row in reader:
         print(row)
    print 'SIII'+ row[0]
   # return row[0]
