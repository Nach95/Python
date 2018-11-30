#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio Creacion de un password 

# Importamos modulos para obtener letras del abecedario mayusculas y minusculas para generar letras
#aleatorias asi como numeros
from string import letters
from random import choice, randint

# Cadena donde se almacenera nuestro password
generada = ''

def password(aux,num,generada):
    '''
    En esta funcion se crea un password utilizando la politica de una longitud de 8 caracteres la cual debe
    de contener un numero, para esto la funcion recibe tres parametros el primero nos ayuda a determinar si
    ya cumplimos con la longitud de 8 caracteres esta variable al iniciar se inicializa en 0 y va aumentando
    de valor conforme se van agregando elementos al password se agregan elementos al password de manera
    recursiva, el segundo parametro es en que posicion estara el numero esta posicion la determinamos
    aleatoriamente de igual manera se le asigna el numero al password, el tercer parametro es la cadena con
    el password generado, primero el programa evalua si la posicion en donde debe de ir el numero es igual
    a la variable aux y si este es menor a 7 si se cumple asigna un numero aleatorio en esa posicion y se
    vuelve a llamar la funcion, la segunda condicion es en caso que el numero se asigne al password se
    encuentre en la ultima posicion si se cumple se asignara el numero al password y se retornara el password
    generado, la tercera condicion es si aun no se cumple longitud se va agregar una letra en esa posicion
    al password y se vuelve a llamar la funcion si no se cumple una de las anteriores condiciones entonces
    ya se ah creado el password y retornamos el password generado
    '''
    if num == aux and aux < 7:
        generada = generada + str(randint(0,9))
        return password(aux+1,num,generada)
    elif num == aux and aux == 7:
        generada = generada + str(num)
        return generada
    elif aux < 8:
        generada = generada + choice(letters)
        return password(aux+1,num,generada)
    else:
        return generada

# Posicion en el password donde se guardara un numero
num = randint(0,7)
print "El password generado de 8 elementos es:",
print password(0,num,generada)
