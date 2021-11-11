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
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

dirfile = 'UFOS-utf8-large.csv'
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
        
        print("===================Req No.1 Inputs===================")
        ciudad = input("Escriba el Nombre de la ciudad que quiere conocer sus avistamientos: ")
        start = time.time()
        tamano, altura , numsights, list5most, list5mostnum ,list3firstandlast= controller.contarAvistamientos(cont,ciudad)
        sightingsEnCiudad = controller.getNumSightsCities(cont,ciudad)
        print("===================Req No.1 Answer===================")
        print("There are ", numsights, " Different cities with UFO sightings")
        print("The top 5 cities with the most UFO sightings are:")
        table = PrettyTable(['City','Sightings'])
        for i in range(1,6):
            table.add_row([lt.getElement(list5most,i),lt.getElement(list5mostnum,i)])
        print(table)

        print()
        print('There are ',sightingsEnCiudad, ' sightinings in ', ciudad, ' city.')
        print('The first 3 and last 3 Sightings for ', ciudad, ' city are:')
        table2 = PrettyTable(['datetime','city','state','country','shape','duration(seconds)'])
        iterador = lt.iterator(list3firstandlast)
        for sighting in iterador:
            table2.add_row([sighting['datetime'],sighting['city'],sighting['state'],sighting['country'],sighting['shape'],sighting['duration (seconds)']])
        print(table2)
        end = time.time()
        print(end - start)

    elif int(inputs[0]) == 4:
        

        smin = int(input('Ingrese la duración mínima: '))
        smax = int(input('Ingrese la duración máxima: '))
        start = time.time()
        result = controller.eventoDuracion(cont,smin,smax)

        print('=============== Req No.2 Inputs ===============')
        print('UFO sightings between ' + str(smin) + ' and ' + str(smax))
        print('')
        print('There are ' + str(result[0]) + ' different durations of UFO sightings....')
        print('The longest UFO sightings are:')

        table3 = PrettyTable(['duration (seconds)', 'count'])
        table3.add_row([result[1][0], result[1][1]])

        print(table3)
        print('')
        print('There are ' + str(result[2]) + ' sightings between: ' + str(smin) + ' and ' + str(smax) + ' duration.')
        print('The first 3 and last 3 UFO sightings in the duration time are:')

        table4 = PrettyTable(['datetime', 'city', 'state', 'country', 'shape', 'duration (seconds)'])

        it1 = lt.iterator(result[3])
        for element in it1:
            table4.add_row([element['datetime'], element['city'], element['state'], element['country'], element['shape'], element['duration (seconds)']])

        it2 = lt.iterator(result[4])
        for element in it2:
            table4.add_row([element['datetime'], element['city'], element['state'], element['country'], element['shape'], element['duration (seconds)']])

        print(table4)
        end = time.time()
        print(end - start)
        

    elif int(inputs[0]) == 5:

        
        print("===================Req No.3 Inputs===================")

        print('Ingrese el limite inferior en formato HH:MM')
        limMin = input()
        print('Ingrese el limite superior en formato HH:MM')
        limMax = input()
        start = time.time()
        listaResp = controller.getHorasAvistamiento(cont, limMin, limMax)
        numDifTimes = controller.getNumSights(cont)
        sizeLatestSight = controller.getsizeLatestSight(cont)
        eventofinal = controller.getLastTimeEvent(cont)
        # Cosas para los prints
        print("UFO sightings between ",limMin," and ", limMax)
        print()
        print("===================Req No.3 Answer===================")
        print("There are", numDifTimes ,"UFO sightings with different times [hh:mm:ss]")
        print("The latest UFO sightings time is: ")

        table69 = PrettyTable(['Time','Count'])
        tiempoeventofinal = eventofinal['datetime']
        listaeventofinal = tiempoeventofinal.split()
        table69.add_row([listaeventofinal[1],sizeLatestSight])
        print(table69)


        table = PrettyTable(['DateTime','Time','City','State','Country','Shape','Duration(seconds)'])
        ## Poner en la pretty table los primeros 3
        for i in range(1,4):
            evento = lt.getElement(listaResp, i)
            tiempo = evento['datetime']
            tiempo = tiempo.split()
            tiempo = tiempo[1]
            table.add_row([evento['datetime'],tiempo,evento['city'],evento['state'],evento['country'],evento['shape'],evento['duration (seconds)']])
        ## Poner en la pretty table los ultimos 3
        for i in range(lt.size(listaResp)-3,lt.size(listaResp)):
            index = 3-i
            evento = lt.getElement(listaResp,i+1)
            tiempo = evento['datetime']
            tiempo = tiempo.split()
            tiempo = tiempo[1]
            table.add_row([evento['datetime'],tiempo,evento['city'],evento['state'],evento['country'],evento['shape'],evento['duration (seconds)']])
        print(table)

        end = time.time()
        print(end - start)

    elif int(inputs[0]) == 6:

        print("===================Req No.4 Inputs===================")

        print('Ingrese el limite inferior en formato [YYYY-MM-DD]')
        limMin = input()
        print('Ingrese el limite superior en formato [YYYY-MM-DD]')
        limMax = input()
        start = time.time()
        listaResp = controller.getDatesAvistamiento(cont, limMin, limMax)
        numDifTimes = controller.getNumSightsDates(cont)
        sizeLatestSight = controller.getsizeLatestSightDatesDates(cont)
        eventofinal = controller.getLastTimeEventDates(cont)
        # Cosas para los prints
        print("UFO sightings between ",limMin," and ", limMax)
        print()
        print("===================Req No.4 Answer===================")
        print("There are", numDifTimes ,"UFO sightings with different times [YYYY-MM-DD]")
        print("The oldest UFO sightings date is: ")

        table69 = PrettyTable(['Date','Count'])
        tiempoeventofinal = eventofinal['datetime']
        listaeventofinal = tiempoeventofinal.split()
        table69.add_row([listaeventofinal[0],sizeLatestSight])
        print(table69)

        table = PrettyTable(['DateTime','Date','City','State','Country','Shape','Duration(seconds)'])
        ## Poner en la pretty table los primeros 3
        for i in range(1,4):
            evento = lt.getElement(listaResp, i)
            tiempo = evento['datetime']
            tiempo = tiempo.split()
            tiempo = tiempo[0]
            table.add_row([evento['datetime'],tiempo,evento['city'],evento['state'],evento['country'],evento['shape'],evento['duration (seconds)']])
        ## Poner en la pretty table los ultimos 3
        for i in range(lt.size(listaResp)-3,lt.size(listaResp)):
            index = 3-i
            evento = lt.getElement(listaResp,i+1)
            tiempo = evento['datetime']
            tiempo = tiempo.split()
            tiempo = tiempo[0]
            table.add_row([evento['datetime'],tiempo,evento['city'],evento['state'],evento['country'],evento['shape'],evento['duration (seconds)']])
        print(table)
        end = time.time()
        print(end - start)

    elif int(inputs[0]) == 7:

        
        long1 = round(float(input('Ingrese el valor minimo de longitud')), 2)
        long2 = round(float(input('Ingrese el valor máximo de longitud')), 2)
        lat1 = round(float(input('Ingrese el valor minimo de latitud')), 2)
        lat2 = round(float(input('Ingrese el valor máximo de latitud')), 2)
        start = time.time()

        result = controller.geoviews(cont, long1, long2, lat1, lat2)
        
        
        print('=============== Req No.5 Inputs ===============')
        print('UFO sightings between latitude range of ' + str(lat1) + ' and ' + str(lat2))
        print('plus longitude of ' + str(long1) + ' and ' + str(long2))
        print('')

        print('=============== Req No.5 Inputs ===============')
        print('There are ' + str(result[0]) + ' different UFO sightings in the current area')
        print('The first 5 and last 5 UFO sightings in this time are:')

        table7 = PrettyTable(['datetime', 'city', 'state', 'country', 'shape', 'duration (seconds)', 'latitude', 'longitude'])

        it7 = lt.iterator(result[1])
        for element in it7:
                    table7.add_row([element['datetime'], element['city'], element['state'], element['country'], element['shape'], element['duration (seconds)'], element['latitude'], element['longitude']])

        print(table7)
        end = time.time()
        print(end - start)

    else:
        sys.exit(0)
sys.exit(0)

