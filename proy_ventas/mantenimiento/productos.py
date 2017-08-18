import sys
sys.path.append('..')
from data.clsConexion import conexion

def insertarDatos():
	con=conexion()
	cursor = con.cursor()
	
	nombre =input("Ingrese el nombre del producto: ")
	precio =input("Ingrese el precio del producto: ")

	valores = "INSERT INTO producto(nombre_producto,precio_producto,estado_producto) VALUES ('"+nombre+"',"+precio+",'1')"
	
	try:
		cursor.execute(valores)
		con.commit()
		print("Se han insertado los valores correctamente")
	except:
		print("Eror, no se han insertado los valores correctamente")
	finally:
		con.close()
		print("Se cerró la conexión")
