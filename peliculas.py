# import random 


# pelicula = {
#     "codigo": "139802789312",
#     "nombre": "nombre uwu"
# }

# nombre = "pelicula 1"
# anio = "2000"
# categoria = "pelicula 1"
# lista_actores = ['leo', 'maria']
# director = "director 1"

# agregar actores a la lista de actores 
# cantidad_actores = 2

# for i in range(2):
#     actor = input("ingresa un actor: ")
#     lista_actores.append(actor)

# print(lista_actores)

#----------------------------------------------------------------------------- 

# lista de diccionarios
# lista_peliculas = [
#     {
#         "codigo": "139802789312",
#         "nombre": "nombre uwu"
#     },
#     {
#         "codigo": "139802789312",
#         "nombre": "pelicula 2 uwu"
#     },
#     {
#         "codigo": "139802789312",
#         "nombre": "nombre uwu"
#     }
# ]

# print(lista_peliculas[1]["codigo"])

#----------------------------------------------------------------------------- 

# lista_peliculas = []

# # pedir los datos al usuario

# diccionario_pelicula = {
#         "codigo": "139802789312",
#         "nombre": "nombre uwu"
#     }

# lista_peliculas.append(diccionario_pelicula)
# lista_peliculas.append(diccionario_pelicula)

# print(lista_peliculas)

#----------------------------------------------------------------------------- 
# Desarrollo ejercicio
# import random 

# # 1. agregar pelicula

# lista_peliculas = []

# def menu():
#     print("Menu\n")
#     print("1. Agregar pelicula")
#     print("2. Lista peliculas")
#     print("3. Buscar pelicula")
#     print("4. Salir")


# def agregar_pelicula():
#     # declaro variable lista
#     lista_actores = []
    
#     # pido los datos de la pelicula
#     nombre = input("Ingresa el nombre: ")
#     anio = input("Ingresa el año: ")
#     categoria = input("Ingresa la categoria: ")

#     cantidad_actores = int(input("Ingresa la cantidad de actores: "))
#     for i in range(cantidad_actores):
#         actor = input(f"Ingresa el actor {i+1}: ")
#         lista_actores.append(actor)

#     director = input("Ingresa el director: ")

#     pelicula = {
#         "codigo": random.randint(1,1000),
#         "nombre": nombre,
#         "año": anio,
#         "categoria": categoria,
#         "actores": lista_actores,
#         "director": director
#     }
#     # print(pelicula)
#     return pelicula

# # pelicula = agregar_pelicula()
# # lista_peliculas.append(pelicula)
# # lista_peliculas.append(agregar_pelicula())

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

# def listar_peliculas():

#     for index, pelicula in enumerate(lista_peliculas):
#         print(f"Pelicula {index+1}: ",pelicula["nombre"])

# # listar_peliculas()

# def buscar_peliculas():

#     buscar_categoria = input("Ingresa una categoria a buscar: ") 

#     for index, pelicula in enumerate(lista_peliculas):
#         if pelicula["categoria"] == buscar_categoria:
#             print("Categoria encontrada")
#             print(f"Pelicula n°{index+1}\n")
#             print(pelicula)

# # buscar_peliculas()

# # genera archivo de texto con las peliculas 
# with open("peliculas.txt","w") as archivo:
#     for pelicula in lista_peliculas:
#         archivo.write(f"{pelicula}\n")
 