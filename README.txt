Vytis Karanauskas 201912961
Nicolas Caicedo 201820789


PREGUNTAS:
¿Qué estructura debería tener el catálogo?
- Vamos a empezar con un diccionario que va a contener tres llaves: movies, directors y actors. Cada llave va a tener de valor una lista, vamos a trabajar con ArrayList
  ya que estas pueden ser un poco mas rápidas de recorrer y agregar elementos. Cada lista va a tener en su interior diccionarios con información relevante.

¿Qué hacer al procesar cada línea de cada uno de los archivos?
- Toma el nombre de la columna y se lo asigna a una llave. El valor de cada llave es el dato de la columna y la fila que está recorriendo.

¿Se debería ordenar la información?
- Sí, al tener ordenados los datos se pueden cumplir requerimientos a mayor velocidad. Ejemplo: requerimiento de mejores y peores películas; de no estar ordenadas se tendría que recorrer la lista múltiples veces.

¿Cómo usar la menor cantidad de memoria posible?
- Creando la menor cantidad de listas y variables, usando algoritmos de ordenamiento que usen poco espacio y guardando solo datos relevantes. No guardar la indormación más de una vez.

¿Cómo se pueden utilizar las estructuras de datos vistas en clase?
- Podemos variar entre arrays y singleliked para recorrer los datos más rápidamente. Esto va a depender si solo vamos a recorrer o también tenemos que agregar al final, al comienzo o contar.
