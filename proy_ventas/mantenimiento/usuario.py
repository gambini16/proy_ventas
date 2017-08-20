import sys

sys.path.append('..')
from data.clsConexion import conexion

def insertarDatos(nombre_usuario, password_usuario):
    con = conexion()
    cursor = con.cursor()

    valores = "INSERT INTO usuario(nombre_usuario,password_usuario,estado_usuario) VALUES ('" + nombre_usuario + "'," + password_usuario + ",'1')"

    try:
        cursor.execute(valores)
        con.commit()
        print("Se han insertado los valores correctamente")
    except:
        print("Eror, no se han insertado los valores correctamente")
    finally:
        con.close()


def actualizarDatos(id_usuario, nombre_usuario):
    con = conexion()
    cursor = con.cursor()

    valores = "UPDATE  usuario SET nombre_usuario='" + nombre_usuario + "' WHERE id_usuario=" + id_usuario + " "

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

    valores = "DELETE FROM usuario " + " WHERE id_usuario=" + id_usuario + " "

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

    cursor.execute("SELECT id_usuario,nombre_usuario,password_usuario FROM usuario")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()