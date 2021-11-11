"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import iterator
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():

    catalog = { 'events': None,
                'dates': None,
                'durations': None,
                'hours': None,
                'locations': None}

    catalog['events'] = lt.newList('SINGLE_LINKED')
    
    catalog['dates'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    catalog['durations'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDuration)
    catalog['hours'] = om.newMap(omaptype='RBT')
    catalog['locations'] = mp.newMap(1000,
                                  maptype='PROBING',
                                  loadfactor=0.5)
    catalog['latlong'] = om.newMap(omaptype='RBT',
                                  comparefunction=compareLong)

    return catalog

def addEvent(catalog, event):
    #event
    lt.addLast(catalog['events'], event)

    #date
    
    updateDateIndex(catalog['dates'], event)
    #duration

    updateDurationIndex(catalog['durations'], event)
    #hour

    updateHourIndex(catalog['hours'], event)

    #location
    addLocation(catalog['locations'], event)

    addLatLong(catalog['latlong'], event)

    return catalog

def updateDurationIndex(mapa, event):
    duration = float(event['duration (seconds)'])
    try:
        arbol = me.getValue(om.get(mapa,duration))
    except:
        arbol = lt.newList('ARRAY_LIST',cmpfunction = compareCities)
    lt.addLast(arbol, event)
    om.put(mapa,duration,arbol)

def updateDateIndex(arbol, event):
    """
    Formato de las Dates: event['datetime'] = '2009-09-12 21:05:00'
    """
    date = event['datetime']
    listdates = date.split()
    listTime = listdates[0].split('-')
    timer = time.strptime(listdates[0], "%Y-%m-%d")
    years = int(listTime[0])
    totalTime = years *365 + int(timer[7])
    ## TotalTime va a ser la key que vamos a usar en el arbol principal
    try:
        dupla = om.get(arbol,totalTime)
        subarbol = me.getValue(dupla)
    except:
        subarbol = om.newMap(omaptype='RBT')
    
    ## Ya dentro del arbol y con el subarbol encontrado necesitamos adicionar el evento a este subarbol
    # necesitamos encontrar el time in day para guardarlo aqui TotalTimeInDay = ?
    listHours = listdates[1].split(':')
    hours = listHours[0]
    mins = listTime[1]
    TotalTimeInDay = int(hours)*60 + int(mins)

    om.put(subarbol,TotalTimeInDay,event)
    om.put(arbol,totalTime,subarbol)

    

def addLatLong(mapa, event):
    longitude = round(float(event['longitude']),2)
    latitude = round(float(event['latitude']),2)
    try:
        arbol = me.getValue(om.get(mapa,longitude))
        lista = me.getValue(om.get(arbol,latitude))


    except:
        arbol = om.newMap(omaptype='RBT',
                        comparefunction=compareLat)
        lista = lt.newList('ARRAY_LIST')


    lt.addLast(lista, event)

    om.put(arbol,latitude,lista)
    om.put(mapa,longitude,arbol)

def updateHourIndex(arbol, event):
    """
    Formato de las Dates: event['datetime'] = '2009-09-12 21:05:00'
    """
    date = event['datetime']
    listdates = date.split()
    listTime = listdates[1].split(':')
    hours = listTime[0]
    mins = listTime[1]

    # transformar las horas en minutos para guardar en el arbol como llave
    hours = int(hours) * 60

    # unir las horas con los minutos
    llaveMins = hours + int(mins)

    # Guardar en el Arbol de horas
    try:
        # si esta entrada ya existia
        dupla = om.get(arbol,llaveMins)
        subarbol = me.getValue(dupla)

    except:
        # Si la entrada no existia se crea un nuevo arbol para guardar los eventos organizados por fecha
        subarbol = om.newMap(omaptype='RBT',
                              comparefunction=compareDates)

    # Ahora neceistamos poner las fechas en unidades que se puedan leer y guardar en el subarbol el evento
    llaveSubArbol = time.strptime(listdates[0], "%Y-%m-%d")
    anio = int(llaveSubArbol[0]) *365
    llavefinal = int(llaveSubArbol[7]) + anio
    om.put(subarbol,llavefinal,event)
    om.put(arbol,llaveMins, subarbol)



def addDateIndex(datentry, event):\
    b = 'b'

def addLocation(mapa, event):
    location = event['city']
    try:
        arbol = me.getValue(mp.get(mapa,location))
    except:
        arbol = om.newMap(omaptype='RBT',
                        comparefunction=compareDates)
    om.put(arbol,event['datetime'],event)
    mp.put(mapa,location,arbol)

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

def crearArbolCiudades(catalog):
    catalog['cities'] = om.newMap(omaptype='RBT',
                        comparefunction=compareSize)

    keylist = mp.keySet(catalog['locations'])
    iterador = lt.iterator(keylist)
    for ciudad in iterador:
        ## Hacer un arbol que guarde como keys los tamanos de los arboles del anterior diccionario y
        ## guarde como valores los nombres de las ciudades a los que estos arboles pertenecen.
        ## Que pasa si tiene el mismo numero de avistamientos? hago un array que guarde los nombres de todas las ciudades.
        arbol = me.getValue(mp.get(catalog['locations'],ciudad))
        llave = om.size(arbol)
        
        try: 
            lista = me.getValue(om.get(catalog['cities'],llave))
        except:
            lista = lt.newList()
        lt.addLast(lista,ciudad)
        om.put(catalog['cities'],llave,lista)


# Funciones de consulta

def getHorasAvistamiento(cont, limMin, limMax):
    solucion = lt.newList()
    arbol = cont['hours']
    setLlaves = om.values(arbol,limMin,limMax)
    llaves =  lt.iterator(setLlaves)
    for llave in llaves:
        subarbol = llave
        keyssub = om.keySet(subarbol)
        keys = lt.iterator(keyssub)
        for key in keys:
            duplisha = om.get(subarbol,key)
            evento = me.getValue(duplisha)
            lt.addLast(solucion,evento)
    
    return solucion

def getsizeLatestSight(cont):
    solucion = 0
    arbol = cont['hours']
    maxkey = om.maxKey(arbol)
    dupla = om.get(arbol,maxkey)
    subarbol = me.getValue(dupla)
    solucion = om.size(subarbol)
    return solucion

def getNumSights(cont):
    arbol = cont['hours']
    solucion = om.size(arbol)
    return solucion

def getNumSightsCities(cont,ciudad):
    mapa = cont['locations']
    dupla = mp.get(mapa,ciudad)
    arbol = me.getValue(dupla)
    return om.size(arbol)

def getLastTimeEvent(cont):
    arbol = cont['hours']
    maxkey = om.maxKey(arbol)
    dupla = om.get(arbol,maxkey)
    subarbol = me.getValue(dupla)
    maxkey2 = om.maxKey(subarbol)
    dupla2 = om.get(subarbol,maxkey2)
    eventosolucion = me.getValue(dupla2)
    return eventosolucion

## Funciones para Req4
def getDatesAvistamiento(cont, limMin, limMax):
    solucion = lt.newList()
    arbol = cont['dates']
    setLlaves = om.values(arbol,limMin,limMax)
    llaves =  lt.iterator(setLlaves)
    for llave in llaves:
        subarbol = llave
        keyssub = om.keySet(subarbol)
        keys = lt.iterator(keyssub)
        for key in keys:
            duplisha = om.get(subarbol,key)
            evento = me.getValue(duplisha)
            lt.addLast(solucion,evento)
    
    return solucion

def getsizeOldestSightDates(cont):
    solucion = 0
    arbol = cont['dates']
    minkey = om.minKey(arbol)
    dupla = om.get(arbol,minkey)
    subarbol = me.getValue(dupla)
    solucion = om.size(subarbol)
    return solucion

def getNumSightsDates(cont):
    arbol = cont['dates']
    solucion = om.size(arbol)
    return solucion

def getOldestTimeEventDates(cont):
    arbol = cont['dates']
    minkey = om.minKey(arbol)
    dupla = om.get(arbol,minkey)
    subarbol = me.getValue(dupla)
    minkey2 = om.minKey(subarbol)
    dupla2 = om.get(subarbol,minkey2)
    eventosolucion = me.getValue(dupla2)
    return eventosolucion

def eventSize(catalogo):
    """
    Número de crimenes
    """
    return lt.size(catalogo['event'])


def Height(mapa):
    """
    Altura del arbol
    """
    return om.height(mapa)


def Size(mapa):
    """
    Numero de elementos en el indice
    """
    return om.size(mapa)


def minKey(mapa):
    """
    Llave mas pequena
    """
    return om.minKey(mapa)


def maxKey(mapa):
    """
    Llave mas grande
    """
    return om.maxKey(mapa)

def mapsize(mapa):
    return mp.size(mapa)

def getTop5sightscities(catalog):
    resp = lt.newList()
    resp2 = lt.newList()
    keyset = om.keySet(catalog['cities'])
    iterador = lt.iterator(keyset)
    sentinel = 0
    for number in iterador:  
        lista = me.getValue(om.get(catalog['cities'],number))
        iterador2 = lt.iterator(lista)
        for ciudad in iterador2:
            if(sentinel > lt.size(lista)-5):
                lt.addLast(resp,ciudad)
                lt.addLast(resp2, number)
                sentinel +=1

    return resp, resp2

def getlist3firtandlast(catalog,ciudad):
    resp = lt.newList()
    arbol = me.getValue(mp.get(catalog['locations'],ciudad))
    keyset = om.keySet(arbol)
    iterador = lt.iterator(keyset)
    for key in iterador:
        sighting = me.getValue(om.get(arbol, key))
        lt.addLast(resp,sighting)
    return resp

# Funciones utilizadas para comparar elementos dentro de una lista

def compareSize(key1,key2):

    if (key1 == key2):
        return 0
    elif (key1 < key2):
        return 1
    else:
        return -1

def compareDates(date1, date2):

    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareHour(hour1, hour2):
    if (hour1 == hour2):
        return 0
    elif (hour1 > hour2):
        return 1
    else:
        return -1

def compareDuration(duration1, duration2):
    if (duration1 == duration2):
        return 0
    elif (duration1 > duration2):
        return 1
    else:
        return -1


# Funct est1

def eventoDuracion(catalog,smin,smax):
    #obtener máxima duración
    max = (maxKey(catalog['durations']))
    maxsize1 = me.getValue(om.get(catalog['durations'], max))
    maxsize = lt.size(maxsize1)
    mmax = (max, maxsize)
    #obtener valores en rango
    val = om.values(catalog['durations'], smin, smax)
    #iterar lista
    ltiteration = lt.iterator(val)
    #Variables que devolver
    totalsize = 0
    mina = lt.newList('ARRAY_LIST')
    maxa = lt.newList('ARRAY_LIST')
    #Contadores
    minvalues = 0
    maxvalues = 0

    #For de tamaño total y minimos
    for event in ltiteration:
        # For de 3 iteraciones para los 3 primeros valores que encuentre
        if minvalues < 3:
            #Ordenar por pais-ciudad la lista de valores en la duración
            sa.sort(event, compareCities)
            datos = lt.iterator(event)
            for dato in datos:
                #Recorrer cada dato de la lista de la duración
                if minvalues < 3:
                    #Asegura que no se hayan obtenido ya 3 valores minimos
                    lt.addFirst(mina, dato)
                    minvalues = minvalues + 1
                else:
                    break
        #Cuenta el numero total de avistamientos en el rango
        totalsize = totalsize + lt.size(event)


    #While de valores maximos de 3 iteraciones
    while maxvalues < 3:
        evento = lt.lastElement(val)
        sa.sort(evento, compareCities)
        #Se obtiene la ultima duracion registrada 
        while lt.size(evento) > 0:
            #while se revisa la lista de la duracion hasta que no tenga más datos
            if maxvalues < 3:
                #Se asegura que solo se tomen los ultimos 3 datos
                ultima = lt.lastElement(evento)
                lt.addFirst(maxa, ultima)
                lt.removeLast(evento)
                maxvalues = maxvalues + 1
            else:
                break
        lt.removeLast(val)
    #Se obtiene el numero de diferentes duraciones
    durations = om.size(catalog['durations'])

    return durations, mmax, totalsize, mina, maxa

def geoviews(catalog, long1, long2, lat1, lat2):
    val = om.values(catalog['latlong'], long1, long2)
    #iterar lista de arboles
    ltiteration = lt.iterator(val)

    #Contadores
    minvalue = 0
    maxvalue = 0
    totalsize = 0
    #Lista para resultados
    resultf = lt.newList('ARRAY_LIST')
    #Se revisa cada arbol de longitud y de paso calcular minimos
    for long in ltiteration:
        valong = om.values(long, lat1, lat2)
        valongg = lt.iterator(valong)
        #Se revisa cada arbol de latitud
        for key in valongg:
            kk = lt.iterator(key)
            #Se revisa cada valor en la lista de la misma latitud y longitud
            for value in kk:
                #Se revisa que no se haya registrado ya los 5 primeros valores
                if minvalue < 5:
                    lt.addLast(resultf, value)
                    minvalue = minvalue + 1
                totalsize = totalsize + 1
    tt = totalsize - 5
    
    #Se calculan maximos
    while maxvalue < 5 and tt > 0:
        #Se saca la maxima longitud
        event = lt.lastElement(val)
        evento = om.valueSet(event)
        while lt.size(evento) > 0:
            ultima = lt.lastElement(evento)
            ultima = lt.iterator(ultima)
            #Se saca la maxima latitud y revisan los datos de la lista
            for caso in ultima:
                #Si no se han tomado ya todos los valores existentes o tomado 5 valores maximos, se registra
                if maxvalue < 5 and tt > 0:
                    lt.addLast(resultf, caso)
                    lt.removeLast(evento)
                    maxvalue = maxvalue + 1
                    tt = tt - 1
                else:
                    break
                
            
        lt.removeLast(val)
    
    sa.sort(resultf, compareLati)
    
    return totalsize, resultf

    
def compareCities(city1, city2):

    d1 = (city1['country'] + city1['city'])
    d2 = (city2['country'] + city2['city'])

    d1p = d1.replace(' ', '')
    d2p = d2.replace(' ' , '')
    
    return (d1p < d2p)



def compareLong(long1, long2):
    if (long1 == long2):
        return 0
    elif (long1 > long2):
        return 1
    else:
        return -1

def compareLat(lat1, lat2):
    if (lat1 == lat2):
        return 0
    elif (lat1 > lat2):
        return 1
    else:
        return -1

def compareLati(lat1, lat2):
    return(lat1['latitude'] < lat2['latitude'])
# Funciones de ordenamiento
