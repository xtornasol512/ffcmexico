#!/bin/bash
#Levanta un servidor python ligero para pruebas html
#agregar permisos de ejecucion chmod +x servidrotemp.sh

python -m SimpleHTTPServer 8090
print "Servidor subido en http://localhost:8090"
