from utilidades import menu, agregar_pelicula, listar_peliculas, buscar_peliculas, generar_archivo


# lista_peliculas.append(agregar_pelicula())
# pelicula = agregar_pelicula()
# lista_peliculas.append(pelicula)


print("BIENVENIDOS! a continuacion te mostrare el menu:\n")
menu()

lista_peliculas = []

while True:
    
    try:
    
        opcion = int(input("ingrese una opcion que necesite: "))
        
        if opcion == 1:
            agregar_pelicula()
            pelicula_nueva = agregar_pelicula
            lista_peliculas.append(pelicula_nueva)
        

        elif opcion == 2:
            listar_peliculas(lista_peliculas)
        
        elif opcion == 3:
            buscar_peliculas(lista_peliculas)
        
        elif opcion == 4:
            generar_archivo(lista_peliculas)
            print("usted ha salido del menu!")
            
            break
        
        else:
            print("Opcion invalida! intente nuevamente")
            
            
            
    except ValueError:
        opcion = int(input("Dato invalido! ingrese solo numeros, escribe 1 para continuar: "))
 
    except ZeroDivisionError:
        opcion = int(input("Dato invalido! No puedes ingresar 0, Escribe 1 para continuar: "))