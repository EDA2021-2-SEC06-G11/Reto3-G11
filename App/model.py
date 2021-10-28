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
    catalog['hours'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareHour)
    catalog['locations'] = mp.newMap(1000,
                                  maptype='PROBING',
                                  loadfactor=0.5)

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

    return catalog


def updateDateIndex(mapa, event):
    a = 'a'


def updateDurationIndex(mapa, event):
    a = 'a'


def updateHourIndex(mapa, event):
    a = 'a'


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




# Funciones de ordenamiento
