# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:37:54 2020

@author: Diego
"""


def a_power_b(a1):
    pot=1
    cont = 0
    par = 0
    while a1!= 0: #Evalua a para comprobar que sea diferente de 0
        cont+=1   #Cada vez que se ejecute el ciclo se cuenta una potencia mas
        b1=int(input('Ingrese el exponente: ')) 
        pot = 1
        
        for i in range(0,b1):  #Para realizar el calculo de la potencia sin utilizar **
            pot=pot*a1
        if pot%2 == 0:
            par+=1   #Cada vez que potencia sea divisible entre 2, se cuenta como par
        print('La potencia de '+str(a1)+' a la '+str(b1)+' es '+str(pot))
        
        a1=int(input('Ingrese la base de la potencia: ')) #Se vuelve a pedir a al usuario a
                                                          #para ver si ingresa un valor diferente a 0
    
    print('Ya no puede ingresar mas valores')  #El programa mostrara esto cuando a=0 
    print('La cantidad de potencias fue '+str(cont))
    print('La cantidad de resultados pares fue '+str(par))
    
    
#Inicia el codigo pidiendo el valor de a
a=int(input('Ingrese la base de la potencia: '))

#Se envia A como parametro
pot = a_power_b(a)
#Antes se pedia B por fuera de la funcion
#pero para evitar que se pidiera dos veces, se decidio pedir dentro del while que 
#evalua si a es diferente de 0 para realizar la operacion
