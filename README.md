# PruebasPenetracion
# Pruebas de Penetración
Prácticas, tareas y examen realizadas en Pruebas de Penetración.

## Red Team 
**Red team.ctb  Red team.pdf**

_En este documento se muestra todo el proceso de que se lleva acabo en el procesos de reconocimiento._ 

## TTL Ping
**ping.py**

_En este programa se recibe un archivo con direcciones IP una por cada línea y se les realiza un ping determinando por el TTL si se trata
de un sistema operativo Windows o LINUX, ya que dependiendo del valor del TTL sabemos si se trata de un Windows o de un Linux, si el TTL
es menor o igual a 66 es un sistema operativo Linux, si su TTL es menor o igual a 255 o mayor a 128 se trata de un sistema operativo 
Linux y si su TTL es menor o igual a 128 y mayor a 66 se trata de un sistema operativo Windows._
Para ejecutarlo se le pasa un archivo con las direcciones IP a hacerles ping, una dirección IP por cada línea, se ejecuta de la siguiente 
forma:

```
python ping.py -f archivo.txt
```
donde archivo.txt es el archivo que contiene las direcciones IP.

## Enumeracion SMTP
**smtp.py**

_En este programa se realiza una enumeración de usuarios en SMTP, utilizando los comandos VRY y RCPT, el programa recibe una lista de 
usuarios la cual se utilizará para enumerar los usuarios, la dirección IP del objetivo y el método a utilizar ya sea VRFY o RCPT, mostrando
los usuarios validos._
Para ejecutarlo se le pasas un archivo con los usuarios, una dirección IP y el método con el cual se verificarán los usuarios, para 
ejecutarlo con el método VRFY es de la siguiente manera:
```
python smtp.py -t 192.168.1.67 -f usuarios.txt -v 
```
Para ejecutarlo con el método RCPT es de la siguiente manera:
```
python smtp.py -t 192.168.1.67 -f usuarios.txt -r
```

## Escáner de puertos
**escaner.py**

_En este programa se utilizo la biblioteca Scapy de python, lo que realiza el programa es realizar un escaneo de los primeros 1024 puertos 
de la direccion IP que se le paso como parametro, mostrando los puertos que se encuentran abiertos o filtrados._
Para ejecutarlo es de la siguiente manera.
```
python escaner.py -i 192.168.1.67
```

## setoolkit
**setoolkit.pdf**

_En este documento se muestra la realización de la práctica setoolkit que utiliza la herramiento setoolkit, la cual nos permite clonar un 
sitio web y realizar un ataque ARP y DNS spoofing._ 

## Pass-the-hash
**pass-the-hash.pdf**

_En este documento se muestra una investigacion del ataque pass-the-hash._

## Examen
**Reporte Ejecutivo.pdf**

_En este documento se muestra un reporte ejecutivo de las pruebas de penetracion que se realizo a la direccion IP 167.99.232.57, mostrando 
de forma general las vulnerabilidades encontradas en forma de resumen._

**Reporte Tecnico.pdf**

_En este documento se muestra un reporte tecnico de las pruebas de penetracion que se realizo a la direccion IP 167.99.232.57, mostrando
de forma detallada cada vulnerabilidad encontrada, evidencias de cada vulnerabilidad y recomendacion para solucionarla._
