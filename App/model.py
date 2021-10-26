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

    catalog = { 'event': None,
                'date': None,
                'duration': None,
                'hour': None,
                'location': None}

    catalog['event'] = lt.newList('SINGLE_LINKED')
    
    catalog['date'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    catalog['duration'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDuration)
    catalog['hour'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareHour)
    catalog['location'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareLocation)

    return catalog

def addEvent(catalog, event):
    #event
    lt.addLast(catalog['event'], event)

    #date
    
    updateDateIndex(catalog['date'], event)
    #duration

    updateDurationIndex(catalog['duration'], event)
    #hour

    updateHourIndex(catalog['hour'], event)
    #location

    updateLocationIndex(catalog['location'], event)

    return catalog


def updateDateIndex(mapa, event):
    a = 'a'


def updateDurationIndex(mapa, event):
    a = 'a'


def updateHourIndex(mapa, event):
    a = 'a'


def updateLocationIndex(mapa, event):
    a = 'a'



def addDateIndex(datentry, event):\
    b = 'b'
# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

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

# Funciones utilizadas para comparar elementos dentro de una lista

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

def compareLocation(location1, location2):
    if (location1 == location2):
        return 0
    elif (location1 > location2):
        return 1
    else:
        return -1


# Funciones de ordenamiento
