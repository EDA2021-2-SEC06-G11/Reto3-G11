"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import prettytable
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from prettytable import PrettyTable

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

dirfile = 'UFOS-utf8-small.csv'
cont = None

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Req1 - Contar los avistamientos en una ciudad")
    print("4- Req2 - Contar los avistamientos por duración")
    print("5- Req3 - Contar los avistamientos por Hora/Minutos del día")
    print("6- Req4 - Contar los avistamientos en un rango de fechas")
    print("7- Req5 - Contar los avistamientos de una Zona Geográfica")
    print("8- Req6 - BONO - Visualizar los avistamientos de una zona geográfica")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont,dirfile)

    elif int(inputs[0]) == 3:
        ciudad = input("Escriba el Nombre de la ciudad que quiere conocer sus avistamientos: ")
        tamano, altura , numsights, list5most, list5mostnum ,list3firstandlast= controller.contarAvistamientos(cont,ciudad)
        print('Notese que se utilizo el arbol para encontrar el orden de los tamaños de los elementos y no como la estructura directa que guarda la informacion, se me hace mas rapido asi')
        print("El tamaño es: ", tamano)
        print("La altura es: ", altura)
        print("There are ", numsights, " Different cities with UFO sightings")
        print("The top 5 cities with the most UFO sightings are:")
        table = PrettyTable(['City','Sightings'])
        for i in range(1,6):
            table.add_row([lt.getElement(list5most,i),lt.getElement(list5mostnum,i)])
        print(table)

        print()
        print('Sightings for ', ciudad, ' city are:')
        table2 = PrettyTable(['datetime','city','state','country','shape','duration(seconds)'])
        iterador = lt.iterator(list3firstandlast)
        for sighting in iterador:
            table2.add_row([sighting['datetime'],sighting['city'],sighting['state'],sighting['country'],sighting['shape'],sighting['duration (seconds)']])
        print(table2)
    else:
        sys.exit(0)
sys.exit(0)
