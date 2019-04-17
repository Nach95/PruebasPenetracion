#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Leal Gonzalez Ignacio

import ConfigParser
import subprocess
import re
import optparse

def addOptions():
    '''
    Funcion que parsea los datos que se tomen de linea de comandos como opciones para ejecutar el programa
    Devuelve un objeto cuyos atributos son las opciones de ejecucion
    '''
    parser = optparse.OptionParser()
    parser.add_option('-f','--file', dest='file', default=None, help='Indica el archivo con las direcciones IP')
    opts,args = parser.parse_args()
    return opts

def checkOptions(options):
    '''
    Funcion que verifica las opciones minimas para que el programa pueda correr correctamente, en caso de no cumplir con los requerimientos minimos
    el programa termina su ejecucion
    Recibe un objeto con las opciones de ejecucion del programa
    '''
    if options.file is None:
        printError('Debes especificar el archivo con las direcciones IP', True)

def ping(archivo):
    '''
    Funcion que realiza el ping con las direcciones IP que se encuentran en el archivo que se paso como parametro, mostrando cada direccion IP si se encuentra arriba y que sistema operativo tiene ya sea Windows 
    o Linux, en caso contrario mostrara que la direccion IP esta abajo, se realiza el ping por medio de un subproceso y al obtener el resultado se obtiene el ttl lo cual indica que esta arriba, si no tiene ttl 
    signifa que esta abajo y se hacen las comparaciones del ttl para determinar si se trata de un Windows o de un Linux.
    '''
    file = open(archivo, "r")
    for ip in file:
	ip = ip[:-1]
	proc = subprocess.Popen( ['ping', '-c', '3', ip], stdout=subprocess.PIPE)
	stdout, stderr = proc.communicate()
	ttl = re.findall('ttl=\d*', stdout)
	if len(ttl) > 0:
		ttl = ttl[0].split("=")
		ttl = ttl[1]
		if int(ttl) <= 66:
			print "La direccion ip " + ip + " se encuentra arriba y tiene un sistema operativo LINUX \n"
		elif int(ttl) <= 128 and ttl > 66:
			print "La direccion ip " + ip + " se encuentra arriba y tiene un sistema operativo Windows\n"
		elif int(ttl) <= 255 and ttl > 128:
			print "La direccion ip " + ip + " se encuentra arriba y tiene un sistema operativo LINUX\n"
		else:
			print "Error"
	else:
		print "La direccion ip " + ip + " se encuentra abajo :("


if __name__ == '__main__':
    '''
    Funcion principal parecida al main en el lenguaje C, en esta funcion ejecutamos la funcion que verifica si se paso el archivo con las direcciones IP y ejecuta el ping.
    '''
    try:
        opts = addOptions()
        checkOptions(opts)
        ping(opts.file)
    except Exception as e:
        print('Un error ocurrio :(')
        print(e, True)
