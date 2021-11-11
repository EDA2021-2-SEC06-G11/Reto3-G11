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
 """

import config as cf
import model
import csv
import time

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, archivo):
    """
    event['datetime'] = '2009-09-12 21:05:00'
    event['city'] = 'brookfield'
    event['state'] = 'wi'
    event['country'] = 'us'
    event['shape'] = 'triangle'
    event['duration (seconds)'] = '600.0'
    event['datetime (hours/min)'] = '5-10 minutes'
    event['comments'] = 'Two groups of  yellow -orange lights formed a moving&#44 silent triangle that rose into the night sky faded and disappeared'
    event['date posted'] = '2009-12-12 00:00:00'
    event['latitude'] = '43.0605556'
    event['longitude'] = '-88.1063889'
    """
    file = cf.data_dir + archivo
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for avistamiento in input_file:
        model.addEvent(catalog, avistamiento)
    return catalog

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def contarAvistamientos(catalog,ciudad):
    model.crearArbolCiudades(catalog)
    tamanoArbol = model.Size(catalog['cities'])
    alturaArbol = model.Height(catalog['cities'])
    numUFOsights = model.mapsize(catalog['locations'])
    listTop5Sights,listTop5sightsNum  = model.getTop5sightscities(catalog)
    list3firtandlast = model.getlist3firtandlast(catalog,ciudad)
    return tamanoArbol, alturaArbol, numUFOsights, listTop5Sights, listTop5sightsNum, list3firtandlast

def getHorasAvistamiento(cont, limMin, limMax):
    """
    La entrada se debiera ver asi:
    LimMin: 20:45:00
    LimMax: 23:15:00
    """
    arrayMin = limMin.split(':')
    arrayMax = limMax.split(':')
    Min = int(arrayMin[0])*60 + int(arrayMin[1])
    Max = int(arrayMax[0])*60 + int(arrayMax[1])
    return model.getHorasAvistamiento(cont, Min, Max)

def getsizeLatestSight(cont):
    return model.getsizeLatestSight(cont)

def getNumSights(cont):
    return model.getNumSights(cont)

def getNumSightsCities(cont,ciudad):
    return model.getNumSightsCities(cont,ciudad)

def getLastTimeEvent(cont):
    return model.getLastTimeEvent(cont)

def contarAvistamientos(catalog,ciudad):
    model.crearArbolCiudades(catalog)
    tamanoArbol = model.Size(catalog['cities'])
    alturaArbol = model.Height(catalog['cities'])
    numUFOsights = model.mapsize(catalog['locations'])
    listTop5Sights,listTop5sightsNum  = model.getTop5sightscities(catalog)
    list3firtandlast = model.getlist3firtandlast(catalog,ciudad)
    return tamanoArbol, alturaArbol, numUFOsights, listTop5Sights, listTop5sightsNum, list3firtandlast 

## Funciones para Date Req4
def getDatesAvistamiento(cont, limMin, limMax):
    """
    La entrada se debiera ver asi: 2009-09-12
    """
    splitedmin = limMin.split('-')
    timer = time.strptime(limMin, "%Y-%m-%d")
    years = int(splitedmin[0])
    totalTimemin = years *365 + int(timer[7])

    splitedmax = limMax.split('-')
    timer = time.strptime(limMax, "%Y-%m-%d")
    years = int(splitedmax[0])
    totalTimemax = years *365 + int(timer[7])

    return model.getDatesAvistamiento(cont, totalTimemin, totalTimemax)

def getsizeLatestSightDatesDates(cont):
    return model.getsizeOldestSightDates(cont)

def getNumSightsDates(cont):
    return model.getNumSightsDates(cont)

def getLastTimeEventDates(cont):
    return model.getOldestTimeEventDates(cont)

## Est1 Functs
def eventoDuracion(catalog,smin,smax):
    return model.eventoDuracion(catalog,smin,smax)

def geoviews(catalog, long1, long2, lat1, lat2):
    return model.geoviews(catalog, long1, long2, lat1, lat2)

def contarAvistamientos(catalog,ciudad):
    model.crearArbolCiudades(catalog)
    tamanoArbol = model.Size(catalog['cities'])
    alturaArbol = model.Height(catalog['cities'])
    numUFOsights = model.mapsize(catalog['locations'])
    listTop5Sights,listTop5sightsNum  = model.getTop5sightscities(catalog)
    list3firtandlast = model.getlist3firtandlast(catalog,ciudad)
    return tamanoArbol, alturaArbol, numUFOsights, listTop5Sights, listTop5sightsNum, list3firtandlast 