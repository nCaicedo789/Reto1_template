"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'movies':None, 'directors':None, 'actors': None}
    catalog['movies'] = lt.newList('ARRAY_LIST')
    catalog['directors'] = lt.newList('ARRAY_LIST')
    catalog['actors'] = lt.newList('ARRAY_LIST')
    return catalog


def newActor (name, movie_id):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    actor = {'name':'', 'movie_id':''}
    actor ['name'] = name
    actor ['movie_id'] = movie_id
    return actor

def addActor (catalog, actor):
    """
    Adiciona un actor a la lista de actores
    """
    d = newActor(actor['actor1_name'], actor['id'])
    if actor["actor1_name"] != "none":
        lt.addLast(catalog['actors'], d)

    d = newActor(actor['actor2_name'], actor['id'])
    if actor["actor2_name"] != "none":
        lt.addLast(catalog['actors'], d)

    d = newActor(actor['actor3_name'], actor['id'])
    if actor["actor3_name"] != "none":
        lt.addLast(catalog['actors'], d)

    d = newActor(actor['actor4_name'], actor['id'])
    if actor["actor4_name"] != "none":
         lt.addLast(catalog['actors'], d)

    d = newActor(actor['actor5_name'], actor['id'])
    if actor["actor5_name"] != "none":
        lt.addLast(catalog['actors'], d)

def newDirector (name, movie_id):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    director = {'name':'', 'movie_id':''}
    director ['name'] = name
    director ['movie_id'] = movie_id
    return director


def addDirector (catalog, director):
    """
    Adiciona un director a la lista de directores
    """
    d = newDirector (director['director_name'], director['id'])
    lt.addLast (catalog['directors'], d)



# Funciones de consulta

def getMoviesByDirector (catalog, dir_name):


    """
    Retorna las peliculas a partir del nombre del director
    """
    return []

