#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Leal Gonzalez Ignacio
 
import random
from scapy.all import *
import ConfigParser
import optparse

def addOptions():
    '''
    Funcion que parsea los datos que se tomen de linea de comandos como opciones para ejecutar el programa
    Devuelve un objeto cuyos atributos son las opciones de ejecucion
    '''
    parser = optparse.OptionParser()
    parser.add_option('-i','--IP', dest='ip', default=None, help='Indica la direccion IP para hacer el escaneo')
    opts,args = parser.parse_args()
    return opts

def checkOptions(options):
    '''
    Funcion que verifica las opciones minimas para que el programa pueda correr correctamente, en caso de no cumplir con los requerimientos minimos
    el programa termina su ejecucion
    Recibe un objeto con las opciones de ejecucion del programa
    '''
    if options.ip is None:
        printError('Debes especificar la direccion IP para hacer el escaneo', True)

def escaneo(host):
    '''
    Funcion que realiza el escaneo a los primeros 1024 puertos en la direccion IP pasada como parametro, mostrando solo los puertos que se encuentran abiertos, cerrados y cuantos puertos hay filtrados.
    '''
    port_range = range(1,1024)
    filtrado=0
    print "============================Resultados==========================="
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(
            IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0,)     
        if resp is None:
            filtrado=filtrado+1
            #print host + " puerto " + str(dst_port) + " esta filtrado."
     
        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):
                send_rst = sr(
                    IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0,)
                print host + " puerto " + str(dst_port) + " esta abierto."
     
        elif (resp.getlayer(TCP).flags == 0x14):
            print host + " puerto " + str(dst_port) + " esta cerrado."
     
        elif(resp.haslayer(ICMP)):
            if(
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                filtrado=filtrado+1
                #print host + " puerto " + str(dst_port) + " esta filtrado."
    print host + "tiene " + str(filtrado) + "puertos filtrados"


if __name__ == '__main__':
    '''
    Funcion principal parecida al main en el lenguaje C, se ejecutan la funcion que comprueba que se paso una direccion IP como parametro y ejecuta el escaneo de los primeros 1024 puertos.
    '''
    try:
        opts = addOptions()
        checkOptions(opts)
        escaneo(opts.ip)
    except Exception as e:
        print('Un error ocurrio :(')
        print(e, True)