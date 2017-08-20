import sys

sys.path.append('..')
from data.clsConexion import conexion

def insertarDatos(nombre_cliente,ruc_cliente,direccion_cliente):
    con = conexion()
    cursor = con.cursor()

    valores = "INSERT INTO cliente(nombre_cliente,ruc_cliente,direccion_cliente,estado_cliente) VALUES ('" + nombre_cliente + "','" + ruc_cliente + "','" + direccion_cliente + "','1')"

    try:
        cursor.execute(valores)
        con.commit()
        print("Se han insertado los valores correctamente")
    except:
        print("Eror, no se han insertado los valores correctamente")
    finally:
        con.close()


def actualizarDatos(id_cliente, nombre_cliente):
    con = conexion()
    cursor = con.cursor()

    valores = "UPDATE  cliente SET nombre_cliente='" + nombre_cliente + "' WHERE id_cliente=" + id_cliente + " "

    try:
        cursor.execute(valores)
        con.commit()
        print("Se actualizó el valor correctamente")
    except:
        print("Eror, no se han insertado los valores correctamente")
    finally:
        cursor.close()
        con.close()


def eliminarDatos(id_cliente):
    con = conexion()
    cursor = con.cursor()

    valores = "DELETE FROM cliente " + " WHERE id_cliente=" + id_cliente + " "

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

    cursor.execute("SELECT id_cliente,nombre_cliente,ruc_cliente,direccion_cliente FROM cliente")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()