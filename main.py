import helper.conexion as conexion
from helper.config import *

#Conexion a la base de datos
connect = conexion.conectar()
database = connect[0]
cursor = connect[1] 


def menu(): 
    print("\n")
    print("*****BIENVENIDO EN QUE TE PUEDO SERVIR HOY*****")
    print("\n")

    print("1. Registrar Una Contraseña: ")    
    print("2. Buscar una Contraseña: ")
    print("3. Ver Todas Las Contraseña: ")
    print("4. Cambiar Una Contraseña: ")
    print("5. Eliminar Una Contraseña: ")
    print("6. SALIR: ")

while True:
    menu()
    print("\n")

    opcion = int(input("¿Que Tarea Deseas Realizar?: "))

    if opcion == 1:
        registrar()

    elif opcion == 2:
        buscar()

    elif opcion == 3:
        consultaA()

    elif opcion == 4:
        actualizar()

    elif opcion == 5:
        eliminar()

    elif opcion == 6:
        print("Ok. Nos Vemos En Otra Ocasion!!")
        break

    else:
        print("Opcion no es valida!!!")







