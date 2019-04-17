#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Leal Gonzalez Ignacio
 
import ConfigParser
import optparse
import socket

mailfrom=["root", True]

def addOptions():
    '''
    Funcion que parsea los datos que se tomen de linea de comandos como opciones para ejecutar el programa
    Devuelve un objeto cuyos atributos son las opciones de ejecucion
    '''
    parser = optparse.OptionParser()
    parser.add_option('-t','--target', dest='target', default=None, help='Indica la direccion IP para hacer la enumeracion de usuarios SMTP')
    parser.add_option('-f','--file', dest='file', default=None, help='Indica el archivo con los nombres de usuarios para hacer la enumeracion de usuarios SMTP')
    parser.add_option('-v','--vrfy', dest='vrfy', action="store_true", default=None, help='Indica el metodo de enumeracion con el comando VRFY')
    parser.add_option('-r','--rcpt', dest='rcpt', action="store_true", default=None, help='Indica el metodo de enumeracion con el comando RCPT')
    opts,args = parser.parse_args()
    return opts

def checkOptions(options):
    '''
    Funcion que verifica las opciones minimas para que el programa pueda correr correctamente, en caso de no cumplir con los requerimientos minimos
    el programa termina su ejecucion
    Recibe un objeto con las opciones de ejecucion del programa
    '''
    if options.target is None:
        printError('Debes especificar la direccion IP del objetivo', True)
    elif options.file is None:
        printError('Debes especificar el archivo con los nombres de usuarios', True)
    elif options.vrfy is None and options.rcpt is None:
        printError('Debes especificar un metodo de enumeracion', True)

def bsocket(options): 
    '''
    Funcion que crea un socket con la direccion del objetivo en el puerto 25, devuelve la conexion del socket
    '''
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexion.connect((options.target, 25)) 
    return conexion

def cerrarS(s): 
    '''
    Funcion que cierra la conexion del socket
    '''
    s.close()
    s = None

def usuarios(archivo): 
    '''
    Funcion que abre el archivo que le pasamos como parametro y lee los nombres de usuarios y los guarda en un vector y devuelve el 
    arreglo con los nombres de usuario
    '''
    with open(archivo, 'r') as file:
        users = file.read().strip().split('\n') # read all, strip last newline, then split at every newline
    userlist = users # store list of usernames in self.userlist
    return userlist     

def metodo(num, usuario, s):
    '''
    Funcion que recibe tres parametros un entero que es el numero del metodo a verificar 1 para vrfy y 2 para rcpt y el socket y dependiendo
    del valor del metodo se llama a la funcion del metodo para verificar los usuarios
    '''
    if num == 1:
        mvrfy(usuario, s)
    elif num == 2:        
        mrcpt(usuario, s)

def mvrfy(nombre, soc):
    '''
    Funcion que verifica un nombre de usuario valido utilizando el metodo vrfy, recibiendo dos parametros el usuario a verificar y el socket
    '''
    soc.send("VRFY %s\n" %(nombre))
    response = soc.recv(1024)
    if ("250" in response) or ("252" in response): 
        print "Usuario " + nombre + " encontrado"

def mrcpt(nombre, soc):
    '''
    Funcion que verifica un nombre de usuario valido utilizando el metodo rcpt, recibiendo dos parametros el usuario a verificar y el socket
    '''
    if mailfrom[1] == True:
        soc.send("MAIL FROM:%s\n" %(mailfrom[0])) 
        soc.recv(1024)
        mailfrom[1]=False
    soc.send("RCPT TO:%s\n" %(nombre))
    response = sock.recv(1024)
    if "250" in response: 
        print "Usuario " + nombre + " encontrado"

if __name__ == '__main__':
    '''
    Funcion principal parecida al main en el lenguaje C, se ejecutan la funcion que comprueba que se paso una direccion IP como parametro y ejecuta el escaneo de los primeros 1024 puertos.
    '''
    try:
        opts = addOptions()
        checkOptions(opts)
        user = usuarios(opts.file)
        sock = bsocket(opts)
        if opts.vrfy == True:
            met = 1
        elif opts.rcpt == True:
            met = 2
        for i in range(len(user)): # enumerate through usernames
      	    metodo(met, user[i], sock) # call probeTarget() and pass current username
        cerrarS(sock)
    except Exception as e:
        print('Un error ocurrio :(')
        print(e, True)
