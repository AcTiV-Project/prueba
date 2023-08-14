import helper.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1] 


def consultaA():
    cursor.execute("SELECT * FROM cuentas")
    consulta = cursor.fetchall()

    for datos in consulta:
        print(datos)

def registrar():
    plataforma = input("Ingresa el nombre de la plataforma: ")
    contraseña = input("Ingresa la contraseña: ")

    sql = "INSERT INTO cuentas (Plataforma, Contraseña) VALUES(%s, %s)"
    val = (plataforma, contraseña)

    cursor.execute(sql, val)

    database.commit()

    print("\n")
    print(cursor.rowcount, "DATOS GUARDADOS...")

def buscar():
    busqueda = input("Ingresa el nombre de la plataforma: ")

    sql = "SELECT * FROM cuentas WHERE Plataforma = '%s'" %busqueda

    cursor.execute(sql)

    resultados = cursor.fetchall()

    for x in resultados:
        print(x)

def eliminar():
    borrar = input("Ingresa el nombre de la plataforma que desea eliminar. ")

    sql = "DELETE FROM cuentas WHERE Plataforma = '%s'" %borrar
    cursor.execute(sql)

    database.commit()
    print(cursor.rowcount, "Datos(s) Borrados!!")

def actualizar():
    plataforma = input("Ingresa el nombre de la plataforma: ")
    contraseña = input("Ingresa la nueva contraseña: ")

    sql = "UPDATE cuentas SET Contraseña = '%s' WHERE Plataforma = '%s' " % (contraseña, plataforma)

    cursor.execute(sql)

    database.commit()

    print(cursor.rowcount, "Datos(s) Actualizados...")