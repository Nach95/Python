#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-BECARIOS

#Leal Gonzalez Ignacio

def palindromo(cadena):
    '''
    Funcion que recibe una cadena y busca el palindromo mas grande, mediante corrimientos en la cadena, con
    el ciclo for recorremos la cadena dada, en el primer while evaluamos la cadena para buscar el mas grande
    palidromo, si es de longitud par y en el segundo evaluamos el mas grande palidromo si es de longitud
    impar
    '''
    # Variable para la longitud del palindromo mas grande encontrado
    longMax=1

    # Variable donde se guardara la posicion en la cadena donde esta el palindromo mas grande
    inicio=0

    # Longitud de la cadena
    longitud=len(cadena)

    # Variables para el corrimiento de la cadena
    correBajo=0
    correAlto=0

    # Corrimiento de la cadena
    for i in xrange(1, longitud):
        correBajo=i-1
        correAlto=i
        while correBajo >= 0 and correAlto < longitud and cadena[correBajo] == cadena[correAlto]:
            if correAlto - correBajo + 1 > longMax:
                inicio=correBajo
                longMax=correAlto-correBajo+1
            correBajo -= 1
            correAlto += 1

        correBajo=i-1
        correAlto=i+1
        while correBajo >= 0 and correAlto < longitud and cadena[correBajo] == cadena[correAlto]:
            if correAlto - correBajo + 1 > longMax:
                inicio=correBajo
                longMax=correAlto-correBajo+1
            correBajo -= 1
            correAlto += 1

    return inicio,longMax

cadena="somosanitalavalatina"
inicio,longitud=palindromo(cadena)
print "El palindromo mas grande encontrado en la cadena es:",
print cadena[inicio:inicio + longitud]
print "La longitud del palindromo mas grande es:",
print longitud
