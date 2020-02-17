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
    catalog = {'movies':None, 'directors':None, 'actors': None, 'generos':None}
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
    print("In model..")
    peliculas={'peliculas':[], 'vote_aver':0, 'num_peli':0}
    numero = 0
    count=0
    size=lt.size(catalog['directors'])
    size_movies=lt.size(catalog['movies'])
    for i in range(1,size+1):
        if dir_name.lower() == lt.getElement(catalog['directors'],i)['name'].lower():
            count+=1
            numero = lt.getElement(catalog['directors'],i)['movie_id']
            

            for j in range(1,size_movies+1):
                if  numero== lt.getElement(catalog['movies'], j)['id']:
                    peliculas['peliculas'].append(lt.getElement(catalog['movies'], j)['title'])
                    peliculas['num_peli']+=1
                    peliculas['vote_aver']+=float(lt.getElement(catalog['movies'], j)['vote_average'])
    print(count)                   
    peliculas['vote_aver']= round((peliculas['vote_aver'])/(peliculas['num_peli']),2)        

    return(peliculas)


def getMoviesByActor(catalog, act_name):
    act_name = act_name.lower()
    lista_ids = []
    lista_movies = []
    size= lt.size(catalog['actors'])

    for i in range(1, size+1):
        if act_name == lt.getElement(catalog['actors'],i)['name'].lower():
            
            lista_ids.append(lt.getElement(catalog['actors'],i)['movie_id'])
    size_movies= lt.size(catalog['movies'])
    for i in range(0, len(lista_ids)):
        for j in range(1, size_movies+1):
            if lista_ids[i] == lt.getElement(catalog['movies'], j)['id']:
                
                lista_movies.append(lt.getElement(catalog['movies'],j)['title'])
    
    return(lista_movies)

def VoteAverageForActor(catalog, act_name):
    act_name = act_name.lower()
    lista_ids = []
    vote_sum = 0
    size= lt.size(catalog['actors'])

    for i in range(1, size+1):
        if act_name == lt.getElement(catalog['actors'],i)['name'].lower():
            
            lista_ids.append(lt.getElement(catalog['actors'],i)['movie_id'])
    size_movies= lt.size(catalog['movies'])
    for i in range(0, len(lista_ids)):
        for j in range(1, size_movies):
            if lista_ids[i] == lt.getElement(catalog['movies'], j)['id']:
                vote_sum += float(lt.getElement(catalog['movies'],j)['vote_average'])
    if len(lista_ids) != 0:
        vote_average = vote_sum/len(lista_ids)
        return (round(vote_average, 2))
    


def MostDirectedActor(catalog, act_name):
    
    lista_dic = []
    act_name = act_name.lower()
    lista_ids = []
    
    size= lt.size(catalog['actors'])
    for i in range(1, size+1):
        if act_name == lt.getElement(catalog['actors'],i)['name'].lower():
            
            lista_ids.append(lt.getElement(catalog['actors'],i)['movie_id'])
    '''
    for i in range(0, len(lista_ids)):
        lista_dic.append(dic)
    '''
    
    size_directors= lt.size(catalog['directors'])
    for i in range(0, len(lista_ids)):
        for j in range(1, size_directors+1):
            
            
            if str(lista_ids[i]) == lt.size(catalog['directors'])['movie_id']:
                lista_dic.append(lt.size(catalog['directors'])['name'])
                #[i]['director'] = catalog['directors']['elements'][j]['name']

    counter = {x:lista_dic.count(x) for x in lista_dic}

    mayor = ''
    cantidad = 0

    for i in counter:
        if counter[i] > cantidad:
            mayor = i
            cantidad = counter[i]
        
    return mayor

   

def getMoviesByGen(catalog, gen):

    info= {'voto_promedio': 0, 'numero_de_peliculas':0}
    size= lt.size(catalog['movies'])
    for i in range(1,size+1):
        x=lt.getElement(catalog['movies'],i)['genres'].split('|')
        for j in x:
            if j.lower()== gen.lower():
                info['numero_de_peliculas']+=1
                info['voto_promedio']+= float(lt.getElement(catalog['movies'],i)['vote_average'])

    if info['numero_de_peliculas']== 0:
        return 'No se encontro el genero\n'
        
    info['voto_promedio']= round(info['voto_promedio']/info['numero_de_peliculas'],2)
            
    return info



    
