#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import django
import sys
sys.path.append('C:/Users/dell/Desktop/Expert_System/backend')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
from perfumes.models import Rate_Perfume
import xlrd
workbook1 = xlrd.open_workbook('time_score.xlsx').sheets()[0]
workbook2 = xlrd.open_workbook('user_love_score.xlsx').sheets()[0]

def main():
    for i in range(0, 200):
        Rate_Perfume.objects.filter(rank=i+1).update(time_score = workbook1.cell_value(i, 0))
        Rate_Perfume.objects.filter(rank=i+1).update(user_love_score = workbook2.cell_value(i, 0))

if __name__ == '__main__':
	main()
