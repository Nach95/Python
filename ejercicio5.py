#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio

#expresion funcional:
# 1) funcion lambda que sume las tres listas
# 2) filtre la lista resultante para obtener a los que tienen un solo nombre (filter)
# 3) convierta a mayusculas los nombres del resultado anterior (map)
# 4) obtener una cadena con los nombres resultantes, separando los nombres con coma (reduce)
#UNA SOLA EXPRESION

eq1 = ['Juan Manuel','Ignacio','Valeria','Luis Antonio','Pedro Alejandro']
eq2 = ['Diana Guadalupe','Jorge Luis','Jesika','Jesus Enrique','Rafael Alejandro']
eq3 = ['Servando Miguel','Ricardo Omar','Laura Patricia','Isaias Abraham','Oscar']

'''
    Primero con una funcion lambda se suman las tres listas, el resultado de esta operacion es la entrada de la operacion filter la cual solo obtendra los de un solo nombre mediante una condicion de
    que si tienen espacio el nombre no lo guardara en caso contrario si lo guardara, a su vez este resultado sera la entrada del map el cual convertira las letras a mayusculas y por ultimo este
    resultado sera la entrada a reduce el cual concatenara los nombre separandolos con una coma
'''
print reduce(lambda x, y : x + ',' + y, map(lambda nom2: nom2.upper(), filter(lambda nom1: " " not in nom1, (lambda nom,nom1,nom2: nom + nom1 + nom2)( eq1, eq2, eq3))))
