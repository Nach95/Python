#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#Leal Gonzalez Ignacio

# Creamos una lista vacia para guardar los numeros primos
lista = []

def numeroPrimoLista(numero,aux):
    '''
    Funcion para saber si un numero es un numero primo recibimos dos parametros los cuales el primero es el
    numero el cual queremos comprobar si es un numero primo y el siguiente numero es con el haremos la operacion 
    modulo el cual estara en una condicion if, que de cumplirse regresara False, la siguiente condicion evalua  
    el siguiente parametro lo evaluamos si es mayor a la division del numero que queremos evaluar entre dos, si 
    se cumple regresara True, se llamara asi misma si no se cumple una de las condiciones anteriores.
    '''
    if (numero % aux == 0):
        return False
    elif (aux > numero/2):
        return True
    else: 
        return numeroPrimoLista(numero,aux+1)

# Le pedimos al usuario que ingrese un numero para comprobar todos los numeros del rango si son primos
comprobar = input("Cuantos numeros quieres comprobar? ")
comprobar += 1

# Hacemos un ciclo for para verificar de todo el intervalo cuales son numeros primos, si es numero primo lo 
# guardamos en lista
for cont in range(2,comprobar):
    if numeroPrimoLista(cont,2):
        lista.append(cont)

# Imprimimos la lista de numeros primos
print lista
