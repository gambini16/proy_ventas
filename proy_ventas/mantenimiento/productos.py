import sys
sys.path.append('..')
from data.clsConexion import conexion

def insertarDatos(nombre_producto,precio_producto):
	con=conexion()
	cursor = con.cursor()

	valores = "INSERT INTO producto(nombre_producto,precio_producto,estado_producto) VALUES ('"+nombre_producto+"',"+precio_producto+",'1')"
	
	try:
		cursor.execute(valores)
		con.commit()
		print("Se han insertado los valores correctamente")
	except:
		print("Eror, no se han insertado los valores correctamente")
	finally:
		con.close()

def actualizarDatos(id_producto,nombre_producto):
	con=conexion()
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
	con=conexion()
	cursor = con.cursor()
	
	valores = "DELETE FROM producto "+" WHERE id_producto=" + id_producto + " " 
	
	try:
		cursor.execute(valores)
		con.commit()
		print("Se han eliminado los valores correctamente")
	except:
		print("Eror, no se ha eliminado el producto indicado")
	finally:
		con.close()
	
	

def leerDatos():
	con=conexion()
	cursor = con.cursor()
	
	cursor.execute("SELECT id_producto,nombre_producto,precio_producto FROM producto")	
	
	rows = cursor.fetchall()

	for row in rows:
		print(row)

	cursor.close()
	con.close()