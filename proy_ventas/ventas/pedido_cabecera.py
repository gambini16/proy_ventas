import mysql.connector
from mysql.connector import errorcode
import sys

sys.path.append('..')
from data.clsConexion import conexion

    
    
def insertarDatos(id_cliente, id_usuario, id_vendedor, fecha_venta, id_producto, cantidad, precio_unitario):
    con = conexion()
    cursor = con.cursor()

    valores = "INSERT INTO pedido_cabecera(id_cliente,id_usuario,id_vendedor,fecha_venta) VALUES (" + id_cliente + "," + id_usuario + "," + id_vendedor + ",'" + fecha_venta + "')"
            
    try:
        cursor.execute(valores)
        
    
        idPedidoTemporal=str(obtenerIdPedidoCabecera())
        total =str(float(cantidad) * float(precio_unitario))
        
        str_salida=insertarDetalles(idPedidoTemporal,id_producto, cantidad, precio_unitario, total)
        print(str_salida)
        
        if str_salida == "OK":
            con.commit()
            print("Se han insertado los valores de cabecera correctamente")
        else:
            con.rollback()
            print("Error en el detalle")
        
    except mysql.connector.Error as err:
        print("ERROR PED. CABECERA:", err)
        con.rollback()
        sys.exit(2)
    except:
        print("Error desconocido, no se han insertado los valores cabecera")
        con.rollback()
        sys.exit(2)
    finally:
        cursor.close()
        con.close()



    


def insertarDetalles(idPedidoTemporal, id_producto, cantidad, precio_unitario, total):
    con2 = conexion()
    cursor2 = con2.cursor()
    
    valores2 = "INSERT INTO pedido_detalle(id_pedido_cabecera,id_producto,cantidad,precio_unitario,total) VALUES ("+ idPedidoTemporal + ","+ id_producto +","+ cantidad +","+ precio_unitario +","+ total +")"
    
    try:
        cursor2.execute(valores2)
        con2.commit()
        print("Se han insertado los detalles correctamente")
        str_exit="OK"
    except mysql.connector.Error as err:
        print("ERROR PED. DETALLE:", err)
        con2.rollback()
        str_exit="FALLO"
    except:
        print("Error desconocido, no se han insertado los valores detalles")
        con2.rollback()
        str_exit="FALLO"
    finally:
        cursor2.close()
        con2.close()
    return str_exit


def obtenerIdPedidoCabecera():
    con = conexion()
    cursor = con.cursor()

    cursor.execute("SELECT id_pedido_cabecera FROM pedido_cabecera order by id_pedido_cabecera DESC LIMIT 1")

    rows = cursor.fetchall()

    for row in rows:
        id = row[0]

    cursor.close()
    con.close()
    return id


def actualizarDatos(id_producto, nombre_producto):
    con = conexion()
    cursor = con.cursor()

    valores = "UPDATE  producto SET nombre_producto='" + nombre_producto + "' WHERE id_producto=" + id_producto + " "

    try:
        cursor.execute(valores)
        con.commit()
        print("Se actualizó el valor correctamente")
    except:
        print("Eror, no se han insertado los valores correctamente")
    finally:
        con.close()


def eliminarDatos(id_producto):
    con = conexion()
    cursor = con.cursor()

    valores = "DELETE FROM producto " + " WHERE id_producto=" + id_producto + " "

    try:
        cursor.execute(valores)
        con.commit()
        print("Se han eliminado los valores correctamente")
    except:
        print("Eror, no se ha eliminado el producto indicado")
    finally:
        con.close()


def leerDatos():
    con = conexion()
    cursor = con.cursor()

    cursor.execute("SELECT id_producto,nombre_producto,precio_producto FROM producto")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()
