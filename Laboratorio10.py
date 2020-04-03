# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:37:54 2020

@author: Diego
"""


def a_power_b(a,b):
    pot=1
    for i in range(0,b):
       pot=pot*a

    return pot
    

a=int(input('Ingrese la base de la potencia: '))
b=int(input('Ingrese el exponente: '))

pot = a_power_b(a,b)
print('La potencia de '+str(a)+' a la '+str(b)+' es '+str(pot))