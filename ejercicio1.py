#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio

#Variable para guardar la lista de aprobados
aprobados = []

def aprueba_becario(nombre_completo):
    '''
    Esta funcion lo que realiza es recibir un nombre completo y separa el nombre de los apellidos, en un ciclo 
    foreach vamos a pasar el nombre con la primera letra mayuscula para checar si esta en los nombres dentro del
    if, si estan son reprobados y si no esta el nombre son aprobados, vamos a pasar el nombre completo a       
    mayusculas y lo vamos a guardar en aprobados, una vez guardado vamos a ordenarlos.
    '''
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        n=n.capitalize()
        if n in ['Manuel', 'Valeria', 'Alejandro', 'Luis', 'Enrique','Omar','Abraham','Oscar']:
            return False
    nombre_completo=nombre_completo.upper()
    aprobados.append(nombre_completo)
    aprobados.sort()
    return True

def eliminar(aprob,elimina):
   '''
   En esta funcion vamos a eliminar un alumno aprobado, recibiendo la lista de los alumnos aprobados y el nombre 
   completo del alumno en mayusculas a eliminar, primero checamos que el nombre del alumno aparezca en la lista
   de los alumnos aprobados si existe lo eliminamos de la lista y regresamos True si no existe regresamos False
   '''
   existe=elimina in aprob
   if existe:
        aprob.remove(elimina)
        return True
   else:
       return False


#Lista de los nombres de los becarios
becarios = ['Cervantes Varela JUAN MaNuEl',
            'Leal González IgnaciO',
            'Ortiz Velarde valeria',
            'Martínez Salazar LUIS ANTONIO',
            'Rodríguez Gallardo pedro alejandro',
            'Tadeo Guillén DiAnA GuAdAlUpE',
            'Ferrusca Ortiz jorge luis',
            'Juárez Méndez JeSiKa',
            'Pacheco Franco jesus ENRIQUE',
            'Vallejo Fernández RAFAEL alejanDrO',
            'López Fernández serVANDO MIGuel',
            'Hernández González ricaRDO OMAr',
            'Acevedo Gómez LAura patrICIA',
            'Manzano Cruz isaías AbrahaM',
            'Espinosa Curiel OscaR']

#Pasamos nombre completo del becario a la funcion aprueba_becario y nos dice si esta aprobado o reprobado
for b in becarios:
    if aprueba_becario(b):
        print 'APROBADOO: ' + b.upper()
    else:
        print 'REPROBADO: ' + b

#Listamos a los alumnos aprobados
print aprobados

#eliminamos un alumno si esta en la lista de aprobados
eliminar(aprobados,'LEAL GONZÁLEZ IGNACIO')

#print becarios
