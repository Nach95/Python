#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio Ejercicio 6 Diccionario por compresion

'''
Se va a realizar un diccionario por compresion en el cula las llaves son los números odiosos menores a 50 y el valor es una tupla de dos elementos: su representación en binario y su representación en
hexadecimal, un número odioso (odious number) es todo aquél que su representación en binario tiene un número impar de unos, por lo tanto haremos un ciclo for que empiece en uno y termine en 49, a
cada numero se convertira a binario y se contara cuantos unos tiene y se le hara el modulo si da un resultado diferente a cero es un numero odioso y se guarda en el diccionario en caso contrario
no se guardara.
'''
diccionario = {x:(bin(x),hex(x)) for x in range(1,50) if bin(x).count('1') % 2 != 0}

print diccionario
