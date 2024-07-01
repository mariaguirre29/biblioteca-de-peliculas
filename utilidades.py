
# def menu ():
#     print("¡BIENVENIDOS AL LISTADO DE PELICULAS!!\n" )
#     print("1. Agregar peliculas\n2. listar pelicula\n3. Buscar pelicula\n4. Sumar años\n5. Salir")
    
# def lista_peliculas():
#     lista = [ ]
#     lista_actores = [ ]
#     codigo_pelicula = input("Ingrese el codigo de la pelicula: ")
#     nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
#     anio_pelicula = input("Ingrese el año de la pelicula: ")
#     categoria_pelicula = input("Ingrese la categoria de la pelicula: ")
#     actores_pelicula = input("Ingrese a los actores de la pelicula: ")
#     director_pelicula = input("Ingrese el nombre del director de la pelicula: ")
    
#     lista_actores.append(actores_pelicula)
#     lista.append(codigo_pelicula,nombre_pelicula,anio_pelicula,categoria_pelicula,actores_pelicula,director_pelicula)
    
    
    


# lista_peliculas = [
#     {
#         "codigo": random.randint(1,1000),
#         "nombre": "narnia",
#         "año": "2020",
#         "categoria": "cat1",
#         "actores": ["leo","maria"],
#         "director": "director"
#     },
#     {
#         "codigo": random.randint(1,1000),
#         "nombre": "el hombre araña",
#         "año": "2021",
#         "categoria": "cat2",
#         "actores": ["leo","maria"],
#         "director": "director"
#     },
#     {
#         "codigo": random.randint(1,1000),
#         "nombre": "batman",
#         "año": "2022",
#         "categoria": "cat3",
#         "actores": ["leo","maria"],
#         "director": "director"
#     }
# ]
#------------------------------------------------------------------------------------------------------------
    
import random 


# 1. agregar pelicula
def menu():
    
    print("1. Agregar pelicula.")
    print("2. Listar peliculas.")
    print("3. Buscar pelicula.")
    print("4. Salir.")


def agregar_pelicula():
    # declaro variable lista
    lista_actores = []
    
    # pido los datos de la pelicula
    nombre = input("Ingresa el nombre: ")
    anio = int(input("Ingresa el año: "))
    categoria = input("Ingresa la categoria: ")

    cantidad_actores = int(input("Ingresa la cantidad de actores: "))
    for i in range(cantidad_actores):
        actor = input(f"Ingresa el actor {i+1}: ")
        lista_actores.append(actor)

    director = input("Ingresa el director: ")

    pelicula = {
        "codigo": random.randint(1,1000),
        "nombre": nombre,
        "año": anio,
        "categoria": categoria,
        "actores": lista_actores,
        "director": director
    }
    # print(pelicula)
    return pelicula


def listar_peliculas(lista_peliculas):

    for index, pelicula in enumerate(lista_peliculas):
        print(f"Pelicula {index+1}: ",pelicula["nombre"])

# listar_peliculas()

#funcion que busca una pelicula en base a su categoria
def buscar_peliculas(lista_peliculas):

    buscar_categoria = input("Ingresa una categoria a buscar: ") 

    for index, pelicula in enumerate(lista_peliculas):
        if pelicula["categoria"] == buscar_categoria:
            print("Categoria encontrada")
            print(f"Pelicula n°{index+1}\n")
            print(pelicula)
            
# buscar_peliculas()

# genera archivo de texto con las peliculas 
def generar_archivo(lista_peliculas):
    
    with open("peliculas.txt","w") as archivo:
        for pelicula in lista_peliculas:
            archivo.write(f"{pelicula}\n")