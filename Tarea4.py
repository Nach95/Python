#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio XML - parser

import sys
import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib
import csv

def encuentraHijos(archivo):
    '''
    Funcion para encontrar todos los hijos de la raiz del archivo xml, como parametro le pasamos el archivo xml y regresamos una lista de los hijos.
    '''
    hijos = []
    with open(archivo,'r') as hijo:
        root = ET.fromstring(hijo.read())
        hijos.append(root.tag)
        for user in root.iter('*'):
            var = user.tag
            #print user.tag, user.attrib
            if var not in hijos:
                hijos.append(var)
    return hijos

def puertos(archivo):
    '''
    Funcion que recibe como parametro un archivo xml y comprueba si los puertos 22, 53, 80 y 443 estan abiertos, regresando la cantidad de puertos abiertos de los puertos 22, 53, 80 y 443 en
    formato de cadena, primero por host checamos los puertos y comprobamos si el estado de ese puerto esta abierto, si es asi se va sumando.
    '''
    cont = 0
    puerto22 = 0
    puerto53 = 0
    puerto80 = 0
    puerto443 = 0
    with open(archivo,'r') as file:
        root = ET.fromstring(file.read())
        for puerto in root.iter('port'):
            for abierto in puerto.iter('state'):
                aux = puerto.get('portid')
                aux2 = abierto.get('state')
                if aux == '22' and aux2 == 'open':
                    puerto22 += 1
                elif aux == '53' and aux2 == 'open':
                    puerto53 += 1
                elif aux == '80' and aux2 == 'open':
                    puerto80 += 1
                elif aux == '443' and aux2 == 'open':
                    puerto443 += 1
    return str(puerto22), str(puerto53), str(puerto80), str(puerto443)

def hosts(archivo):
    '''
    Funcion que recibe como parametro un archivo xml, para conocer cuantos hosts estan prendidos o apagados, por host se va comprobando su estatus si esta arriba significa que esta prendido y si
    down significa que esta apagado, en cada caso se va a ir sumando uno si esta prendido o esta apagado, regresmos la cantidad de host prendidos y apagados en formato de cadena.
    '''
    prendidos = 0
    apagados = 0
    with open(archivo,'r') as compus:
        root = ET.fromstring(compus.read())
        for estado in root.iter('host'):
            for estatus in estado.iter('status'):
                aux = estatus.get('state')
                if aux == 'up':
                    prendidos += 1
                elif aux == 'down':
                    apagados +=1
    return str(prendidos), str(apagados)

def hostname(archivo):
    '''
    Funcion que recibe como parametro un archivo xml, para conocer cuantos hosts tienen un nombre de dominio, para esto comprobamos si tienen un valor en el hostname si es asi se va sumando uno en
    caso contrario no se suma, regresamos la cantidad de hosts que tienen un nombre de dominio en formato de cadena.
    '''
    cant = 0
    with open(archivo,'r') as nombreHost:
        root = ET.fromstring(nombreHost.read())
        for nom in root.iter('hostname'):
            nombre = nom.attrib
            if nombre != 'None':
                cant += 1
    return str(cant)

def servicio(archivo):
    '''
    Funcion que recibe como parametro un archivo xml, para conocer que servicio http tiene activado ya sea apache, si es honeypot, nginx u otro servicio, para esto debemos de obtener por cada
    host el puerto 80, 443 y obtner el servicio que tiene ese puerto ya sea apache, honeypot, nginx u otro, si en el host en los dos puertos tiene activado el mismo servicio solo se toma uno
    por cada servicio se va a sumar uno, se va a regresar la cantidad de host que usan cada servicio en formato de cadena.
    '''
    apache = 0
    honey = 0
    nginx = 0
    otros = 0
    with open(archivo,'r') as nombreHost:
        root = ET.fromstring(nombreHost.read())
        for nom in root.iter('ports'):
            apache80 = 0
            honey80 = 0
            nginx80 = 0
            otros80 = 0
            apache443 = 0
            honey443 = 0
            nginx443 = 0
            otros443 = 0
            for port in nom.iter('port'):
                for serv in port.iter('service'):
                    puerto = port.get('portid')
                    if serv.get('product') and puerto == '80':
                        service = serv.get('product')
                        #print puerto, serv.get('product')
                        if 'Apache' in service:
                            apache80 += 1
                        elif service == 'Dionaea Honeypot httpd':
                            honey80 += 1
                        elif service == 'nginx':
                            nginx80 += 1
                        else:
                            otros80 += 1
                    if serv.get('product') and puerto == '443':
                        service = serv.get('product')
                        if 'Apache' in service:
                            apache443 += 1
                        elif service == 'Dionaea Honeypot httpd':
                            honey443 += 1
                        elif service == 'nginx':
                            nginx443 += 1
                        else:
                            otros443 += 1
            apach = apache80 + apache443
            hone = honey80 + honey443
            ngin = nginx80 + nginx443
            otro = otros80 + otros443
            if apach == 2 or apach == 1:
                apache += 1
            elif hone == 2 or hone == 1:
                honey += 1
            elif ngin == 2 or ngin == 1:
                nginx += 1
            elif otro == 2 or otro == 1:
                otros += 1
    return str(apache), str(honey), str(nginx), str(otros)

def elementos_CSV(archivo):
    '''
    Funcion que recibe como parametro un archivo xml, para conocer la ip de los hosts prendidos, apagados, con el puerto 22 abierto, si son honeypot y cuales tiene un nombre de dominio para esto
    se va a implementar las funciones anteriores y se va a ir guardando en listas las ip's que esten prendidos, apagados, con el puerto 22 abierto, si son Honeypot, cuales tienen un nombre de
    dominio y su nombre de dominio, cada una en diferente lista, se a regresar todas las listas prendidos, apagados, puerto22, honey, dominio y el nombreDominio, todo esto servira para crear un
    archivo csv.
    '''

    prendidos = []
    apagados = []
    puerto22 = []
    honey = []
    dominio = []
    nombreDominio = []
    with open(archivo,'r') as compus:
        root = ET.fromstring(compus.read())
        for estado in root.iter('host'):
            for estatus in estado.iter('status'):
                onOff = estatus.get('state')
                for ip in estado.iter('address'):
                    dir = ip.get('addr')
                    if onOff == 'up':
                        prendidos.append(dir)
                    elif onOff == 'down':
                        apagados.append(dir)
                    for puerto in estado.iter('port'):
                        port = puerto.get('portid')
                        for aux in puerto.iter('state'):
                            servicio = aux.get('state')
                            if port == '22' and servicio == 'open':
                                puerto22.append(dir)
                        for aux2 in puerto.iter('service'):
                            miel = aux2.get('product')
                            if miel == 'Dionaea Honeypot httpd':
                                if dir not in honey:
                                    honey.append(dir)
                    for nombre in estado.iter('hostname'):
                        nom = nombre.attrib
                        if nombre != 'None':
                            nameHost = nombre.get('name')
                            dominio.append(dir)
                            nombreDominio.append (nameHost)
    return prendidos, apagados, puerto22, honey, dominio, nombreDominio

def escribirCSV(prendidos, apagados, puerto22, honey, dominio, nombreDominio):
    '''
    Funcion que recibe como parametro las listas con las ip's de los hosts que estan prendidos, apagados, con el puerto22 abierto, si son honeypot, si tienen un nombre dominio con el nombre de
    dominio, escribiendolo en un archivo csv.
    '''
    with open('reporte.csv', 'a') as csvfile:
        escribir = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for off in apagados:
            escribir.writerow([off, 'Host apagado'])
        for on in prendidos:
            escribir.writerow([on, 'Host prendido'])
        for port in puerto22:
            escribir.writerow([port, 'Host con el puerto 22 abierto'])
        for miel in honey:
            escribir.writerow([miel, 'Host Honeypot'])
        for hostname in dominio:
            escribir.writerow([dominio, nombreDominio])

def escribir(archivo, cadena, variable):
    '''
    Funcion que recibe como parametro un nombre del archivo, una cadena de texto y un numero en formato de cadena, estos parametros sirven para indicar el archivo el cual sera nuestro reporte,
    el cual escribira dentro del archivo la cadena de texto y el numero todo esto para generar un reporte.
    '''
    with open(archivo,'a') as output:
        output.write(cadena + variable + '\n')

def md5(archivo):
    '''
    Funcion que recibe como parametro un archivo xml para sacarle su MD5, regresando el MD5 del archivo en hexadecimal.
    '''
    return hashlib.md5(archivo).hexdigest()

def hora():
    '''
    Funcion que devuelve la hora en que se esta ejecutando el script.
    '''
    return str(datetime.now())

def sha1(archivo):
    '''
    Funcion que recibe como parametro un archivo xml para sacarle su SHA1, regresando el SHA1 del archivo en hexadecimal.
    '''
    return hashlib.sha1(archivo).hexdigest()

if __name__ == '__main__':
# Textos que se mostraran en consola y se escribiran en el archivo de reporte
    texto1 = "Hora de ejecucion: "
    texto2 = "MD5 del archivo XML: "
    texto3 = "SHA1 del archivo XML: "
    texto4 = "Hosts prendidos: "
    texto5 = "Hosts apagados: "
    texto6 = "Hosts con puerto 22 abierto: "
    texto7 = "Hosts con puerto 53 abierto: "
    texto8 = "Hosts con puerto 80 abierto: "
    texto9 = "Hosts con puerto 443 abierto: "
    texto10 = "Hosts que tienen nombre de dominio: "
    texto11 = "Servidores HTTP usados Apache: "
    texto12 = "Servidores HTTP usados Honeypots: "
    texto13 = "Servidores HTTP usados Nginx: "
    texto14 = "Servidores HTTP usados otros: "

# Texto que se mostrara indicandonos el nombre del archivo csv con el reporte mas detallado
    texto15 = "Se creo un archivo llamado reporte.csv donde esta mas detallado el analisis"

# Parametros de entrada a la hora de ejecutar el script el primero es el archivo xml y el segundo es un archivo en donde se escribira el reporte
    xml = sys.argv[1]
    reporte = sys.argv[2]
    #hijos = encuentraHijos(xml)
    #print hijos
# Funciones para obtener los valores que se escribiran en el reporte
    md = md5(xml)
    tiempo = hora()
    hash = sha1(xml)
    prendido, apagado = hosts(xml)
    p23, p53, p80, p443 = puertos(xml)
    nombres = hostname(xml)
    apache, honey, nginx, otros = servicio(xml)
# Funcion para obtener los elementos para escribir el archivo csv un reporte mas detallado
    prendidos, apagados, puerto22, honey2, dominio, nombreDominio = elementos_CSV(xml)

# Escribir en el archivo del reporte
    escribir(reporte, texto1, tiempo)
    escribir(reporte, texto2, md)
    escribir(reporte, texto3, hash)
    escribir(reporte, texto4, prendido)
    escribir(reporte, texto5, apagado)
    escribir(reporte, texto6, p23)
    escribir(reporte, texto7, p53)
    escribir(reporte, texto8, p80)
    escribir(reporte, texto9, p443)
    escribir(reporte, texto10, nombres)
    escribir(reporte, texto11, apache)
    escribir(reporte, texto12, honey)
    escribir(reporte, texto13, nginx)
    escribir(reporte, texto14, otros)

# Escribir en el archivo csv mas detallado
    escribirCSV(prendidos, apagados, puerto22, honey2, dominio, nombreDominio)

# Texto que se mostrara en consola con los resultados
    print texto1, tiempo
    print texto2, md
    print texto3, hash
    print texto4, prendido
    print texto5, apagado
    print texto6, p23
    print texto7, p53
    print texto8, p80
    print texto9, p443
    print texto10, nombres
    print texto11, apache
    print texto12, honey
    print texto13, nginx
    print texto14, otros
    print texto15
