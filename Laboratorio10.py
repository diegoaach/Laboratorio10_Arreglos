# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:37:54 2020

@author: Diego
"""

import numpy as np


def introDatos(a,b,n):   #Funcion para introducir los datos de las potencias que se van a calcular
    
    for i in range (0,n):
        a[i]=int(input('Ingrese la base: '))
        b[i]=int(input('Ingrese su exponente: '))
    
    
def mean_arreglo(a):    #Para calcular el promedio de los valores de un arreglo
    size = len(a)
    acum=0
    for i in range(0,size):
        acum=acum+a[i]
    
    prom=acum/size
    return prom
    
def a_power_b(a, b):
    pot=1
    
    for i in range(0,int(b)):  #Para realizar el calculo de la potencia sin utilizar **
            pot=pot*a
    
    return pot


def std_arreglo(a):  #Funcion para la desviacion de un arreglo
    prom = mean_arreglo(a)
    suma = 0
    n = len(a)
    for x in a:
        suma = suma + abs(x-prom)**2
        
    desviacion = (suma/n)**(1/2)
    
    
    return desviacion


def norm_arreglo(a): #Funcion para normalizar un arreglo
    desv= std_arreglo(a)
    prom = mean_arreglo(a)
    size = len(a)
    print('Valores antes de normalizacion: '+str(a))
    
    for i in range(0,size):
        a[i]=(a[i]-prom)/desv
    
    return a
    
    
    


    
 
 #-------------------------Main------------------------------   


#Inicia el codigo pidiendo el valor de a
n = int(input('Cuantas potencias desea calcular?: '))

bases=[0]*n
expo=[0]*n

a1=np.array(bases)
b1=np.array(expo)

introDatos(a1,b1,n)

#Se envian los arreglos como parametro
par=0
for i in range (0,n):
    pote=a_power_b(a1[i], b1[i])
    if pote%2 == 0:
            par+=1   #Cada vez que potencia sea divisible entre 2, se cuenta como par
    print('La potencia de '+str(a1[i])+' a la '+str(b1[i])+' es '+str(pote))
print('La cantidad de potencias pares fue '+str(par))

    
prom1=mean_arreglo(a1)

prom2=mean_arreglo(b1)

print(prom1)
print(prom2)

potProm=a_power_b(prom1,prom2)
print('La potencia b promedio de a promedio es '+str(potProm))

desv1=std_arreglo(a1)
print('La desviacion estandar de las bases es '+str(round(desv1,5)))
desv2=std_arreglo(b1)
print('La desviacion estandar de los exponentes es '+str(round(desv2,5)))

aNorm=norm_arreglo(a1)
print('Bases despues de la normalizacion'+str(aNorm))

bNorm=norm_arreglo(b1)
print('Exponentes despues de la normalizacion'+str(bNorm))

prom1n=mean_arreglo(a1)
print('Promedio de bases normalizadas: '+str(prom1n))

prom2n=mean_arreglo(b1)
print('Promedio de exponentes normalizadas: '+str(prom2n))

desv1n=std_arreglo(a1)
print('La desviacion de las bases normalizadas: '+str(desv1n))

desv2n=std_arreglo(b1)
print('La desviacion de los exponentes normalizadas: '+str(desv2n))













 





























