#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#Leal Gonzalez Ignacio

def numeroPrimo(numero):
    '''
    Funcion para saber si un numero es un numero primo recibimos un numero como parametro, y vemos si el numero 
    es mayor a dos si se cumple la condicion vamos a hacer un for del rango desde el dos hasta el numero que  
    queremos saber si es primo el cual entrara en la condicion haciendo el modulo del numero que queremos saber
    si es primo con el valor que tome la variable del ciclo for si es 0 va a regresar falso y si no se cumple va 
    a regresar verdadero y sera numero primo 
    '''
    if numero > 2:
        for aux_num in range(2,numero):
            if ( numero % aux_num == 0):
                return False
    else:
	return False
    return True

# Le pedimos que ingrese un numero al usuario
comprobar = int(input('Introduce un numero: '))

# Ejecutamos la funcion numero_primo y dependiendo de la salida va a mostrar si es numero primo o no 
if numeroPrimo(comprobar):
    print '%s Es un numero primo!' % comprobar
else:
    print '%s No es un numero primo!' % comprobar
