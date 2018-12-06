#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio Generador de Diccionarios dado un archivo con palabras

import itertools
from sys import argv
from random import choice

acumulado = []
nueva = []

palabraMayuscula = []
palabraMinuscula = []

palabraMaMi = []
palabraMiMa = []

palabraPosibleMayuscula = []
palabraPosibleMinuscula = []
palabraPosibleMaMi = []

diccionarioLetrasMiMa = {'a':'a4', 'b':'b8', 'c':'c', 'd':'d', 'e':'e3', 'f':'f', 'g':'g6', 'h':'h', 'i':'1', 'j':'j', 'k':'k', 'l':'l1', 'm':'m', 'n':'n', 'o':'o0', 'p':'p', 'q':'q', 'r':'r',
's':'s5', 't':'t7', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z', 'A':'A4', 'B':'B8', 'C':'C(', 'D':'D', 'E':'E3', 'F':'F', 'G':'G6', 'H':'H', 'I':'I1', 'J':'J', 'K':'K', 'L':'L1',
'M':'M', 'N':'N', 'O':'O0', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S5', 'T':'T7', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}

def leer(archivo):
'''
Funcion que recibe como parametro un archivo, el cual contiene las palabras con las cuales generaremos los passwords, regresando una lista con las palabras que tiene el archivo.
'''
    with open(archivo,'r') as palabras:
        lista = [linea.strip() for linea in palabras]
    return lista

def escribir(archivo2,lista):
'''
Funcion que recibe dos parametros, el archivo donde guardaremos los passwords y una lista con los passwords generados que se escribiran en el archivo, comprobando que no se repitan los passwords
para no tener passwords repetidos.
'''
    comprobar = leer(archivo2)
    for aux in lista:
        if aux not in comprobar:
            with open(archivo2,'a') as escritura:
                escritura.write('%s\n' % (aux))

def mayuscula_minuscula(lista):
'''
Funcion que recibe como parametro una lista y devuelve dos listas una escrita con la primera palabra en mayuscula, la siguiente en minuscula, la siguiente en mayuscula y asi sucesivamente, la otra
lista la primera palabra se escribe con minuscula, la siguiente en mayuscula, la siguiente en minuscula y asi sucesivamente.
'''
    cont = 1
    palMayuscula = []
    palMinuscula = []
    for var in lista:
        aux = var.upper()
        aux2 = var.lower()
        palMayuscula.append(aux)
        palMinuscula.append(aux2)
    return palMayuscula, palMinuscula

def miMa(lista):
'''
Funcion que recibe como parametro una lista y devuelve dos listas, una escrita la primera letra de cada palabra en mayuscula, la siguiente letra en minuscula, la siguiente letra en mayuscula y asi
sucesivamente, la otra lista la primera letra de cada palabra en minuscula, la siguiente en mayuscula, la siguiente en minuscula y asi sucesivamente.
'''
    palMaMi = []
    palMiMa = []
    cont = 1
    for palabra in lista:
        cadenaMaMi = []
        cadenaMiMa = []
        for letra in palabra:
            if cont % 2 == 0:
                cadenaMaMi.append(letra.lower())
                cadenaMiMa.append(letra.upper())
                cont += 1
            else:
                cadenaMaMi.append(letra.upper())
                cadenaMiMa.append(letra.lower())
                cont += 1
        palMiMa.append(''.join(cadenaMiMa))
        palMaMi.append(''.join(cadenaMaMi))
    return palMaMi, palMiMa

def palabras_posibles(lista):
'''
Funcion que recibe una lista, por cada palabra va a checar en el diccionario y formara todas las posibles combinaciones con las letras de la palabra que esten en el diccionario almacenandolas en una
nueva lista, cuando pasen todas las palabras de la lista se regresara la lista nueva.
'''
    posible = []
    for palabra in lista:
        cadena = []
        for letra in palabra:
            for simb in diccionarioLetrasMiMa[letra]:
                cadena.append(simb)
            permutacion = []
            var = itertools.combinations(cadena, len(palabra))
            for aux2 in var:
                posible.append(''.join(aux2))
    return posible

def combinaciones(lista):
'''
Funcion que recibe como parametro una lista, y crea todas las posibles combinaciones de dos y tres palabras, almacenandolas en una nueva lista, regresando la lista cuando todas las combinaciones se
hicieron.
'''
    combinadas = []
    for aux in [2,3]:
        var = itertools.combinations(lista, aux)
        for aux2 in var:
            combinadas.append(''.join(aux2))
    return combinadas

def juntar_inicio(lista):
'''
Funcion que recibe como parametro una lista, y por cada palabra tomara la primera letra de cada palabra y las junta para crear una nueva palabra, luego tomara las dos primeras letras, hasta llegar a
tomar tres letras por palabra.
'''
    inicio = []
    for x in range(1,3):
        aux = ''
        for palabra in lista:
            aux = aux + palabra[0:x]
            inicio.append(aux)
    return inicio

def repeticiones(lista1,lista2):
'''
Funcion que recibe dos listas como parametros de entrada, y verifica si no se repiten palabras en las listas, creando una nueva lista sin repeticiones de palabras, regresando esta nueva lista.
'''
    nueva = []
    for palabra1 in lista1:
        if palabra1 not in lista2:
            nueva.append(palabra1)
    return nueva

# Guardamos el nombre del archivo de las palabras y el archivo de los passwords en variables
archivoPalabras = argv[1]
archivoGenerado = argv[2]

lista=leer(archivoPalabras)

escribir(archivoGenerado,lista)

palabraMayuscula, palabraMinuscula = mayuscula_minuscula(lista)
palabraMaMi, palabraMiMa = miMa(lista)

acumulado = acumulado + palabraMayuscula + palabraMinuscula + palabraMaMi + palabraMiMa

escribir(archivoGenerado,acumulado)

palabraPosibleMayuscula = palabras_posibles(palabraMayuscula)

palabraPosibleMinuscula = palabras_posibles(palabraMinuscula)

nueva = repeticiones(palabraPosibleMayuscula, palabraPosibleMinuscula)

palabraPosibleMaMi = palabras_posibles(palabraMaMi)
nueva = nueva + palabraPosibleMaMi
nueva = repeticiones(palabraPosibleMayuscula, palabraPosibleMinuscula)

palabraPosibleMiMa = palabras_posibles(palabraMiMa)
nueva = nueva + palabraMiMa
nueva = repeticiones(palabraPosibleMayuscula, palabraPosibleMinuscula)

palabaraCombinacion = combinaciones(nueva)

escribir(archivoGenerado,palabaraCombinacion)

inicio = juntar_inicio(acumulado)
escribir(archivoGenerado,inicio)
