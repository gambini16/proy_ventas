import sys

sys.path.append('..')
from data.clsConexion import conexion

def insertarDatos(nombre_vendedor):
    con = conexion()
    cursor = con.cursor()

    valores = "INSERT INTO vendedor(nombre_vendedor,estado_vendedor) VALUES ('" + nombre_vendedor + "','1')"

    try:
        cursor.execute(valores)
        con.commit()
        print("Se han insertado los valores correctamente")
    except:
        print("Eror, no se han insertado los valores correctamente")
    finally:
        con.close()


def actualizarDatos(id_vendedor,nombre_vendedor):
    con = conexion()
    cursor = con.cursor()

    valores = "UPDATE  vendedor SET nombre_vendedor='" + nombre_vendedor + "' WHERE id_vendedor=" + id_vendedor + " "

    try:
        cursor.execute(valores)
        con.commit()
        print("Se actualizó el valor correctamente")
    except:
        print("Eror, no se han insertado los valores correctamente")
    finally:
        cursor.close()
        con.close()


def eliminarDatos(id_usuario):
    con = conexion()
    cursor = con.cursor()

    valores = "DELETE FROM vendedor " + " WHERE id_vendedor=" + id_vendedor + " "

    try:
        cursor.execute(valores)
        con.commit()
        print("Se han eliminado los valores correctamente")
    except:
        print("Eror, no se ha eliminado el producto indicado")
    finally:
        cursor.close()
        con.close()


def leerDatos():
    con = conexion()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM vendedor")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()