#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import django
import sys
sys.path.append('C:/Users/dell/Desktop/Expert_System/backend')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
from perfumes.models import Perfume, Rate_Perfume

def main():
    perfumes = Perfume.objects.all()
    for p in perfumes:
        print(p.rank)
        print(p.rate)
        print(int(p.name[-4:]))
        print(p.time)
        print(p.style)
        Rate_Perfume.objects.create(rank=p.rank, rate=p.rate, year=int(p.name[-4:]), time=p.time, style=p.style)

if __name__ == '__main__':
	main()
