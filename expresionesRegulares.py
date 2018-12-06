#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio Ejercicio 7 Expresiones regulares
#Hacer una expresión regular que coincida con una dirección IP versión 4
#Hacer expresión regular que coincida con una dirección de correo electrónico

import re
from sys import argv

# Expresion regular para que coincida con una direccion IPv4
patron = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

# Expresion regular para que coincida con una direccion de correo valida
correo = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"

def validaIP(archivo):
    with open(archivo,'r') as ip:
        for linea in ip:
            if re.findall(patron,linea):
                print linea,
                print "IP valida"
            else:
                print linea,
                print "IP no valida"

def validarCorreo(archivo):
    with open(archivo,'r') as email:
        for linea in email:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',linea):
                print linea,
                print "Correo valido"
            else:
                print linea,
                print "Correo no valido"

#Guardamos el nombre del archivo que contiene las direcciones ip en una variable y el nombre del archivo que contiene las direcciones de correo electronico a validar
ip = argv[1]
correo = argv[2]

validaIP(ip)
validarCorreo(correo)
