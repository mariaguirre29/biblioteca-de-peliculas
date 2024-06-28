def menu ():
    print("¡BIENVENIDOS AL LISTADO DE PELICULAS!!\n" )
    print("1. Agregar peliculas\n2. listar pelicula\n3. Buscar pelicula\n4. Sumar años\n5. Salir")
    
def lista_peliculas():
    lista = [ ]
    lista_actores = [ ]
    codigo_pelicula = input("Ingrese el codigo de la pelicula: ")
    nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
    anio_pelicula = input("Ingrese el año de la pelicula: ")
    categoria_pelicula = input("Ingrese la categoria de la pelicula: ")
    actores_pelicula = input("Ingrese a los actores de la pelicula: ")
    director_pelicula = input("Ingrese el nombre del director de la pelicula: ")
    
    lista_actores.append(actores_pelicula)
    lista.append(codigo_pelicula,nombre_pelicula,anio_pelicula,categoria_pelicula,actores_pelicula,director_pelicula)
    


    