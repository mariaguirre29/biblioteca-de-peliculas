from utilidades import menu, agregar_pelicula, listar_peliculas, buscar_peliculas 

print("BIENVENIDOS! a continuacion te mostrare el menu:\n")
menu()

while True:
    
    try:
        opcion = int(input("ingrese una opcion que necesite: "))
    
        if opcion == 1:
            agregar_pelicula()

        if opcion == 2:
            listar_peliculas()
        
        if opcion == 3:
            buscar_peliculas()
        
        if opcion == 4:
            print("usted ha salido del menu!")
            break
            
        else:
            print("Opcion invalida! intente nuevamente")
            
            
    except ValueError:
        opcion = int(input("Dato invalido! ingrese solo numeros, escribe 1 para continuar: "))
 
    except ZeroDivisionError:
        opcion = int(input("Dato invalido! No puedes ingresar 0, Escribe 1 para continuar: "))