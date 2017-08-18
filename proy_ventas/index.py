import mantenimiento.productos
def Load():
	OpcionesSistemas();
	opcion=input("Ingrese una opción:");
	print("\n");
	
	#MANTENIMIENTO
	if(opcion=="1"):
		OpcionesMantenimiento()
		subopcion=input("Ingrese la subopcion: ")
		
		OpcionesOperaciones(subopcion)
		accion=input("Ingrese la operación: ")

		MantenimientoProducto(accion)
		#mantenimiento.productos.insertarDatos()
	else:
		print("hola")

def MantenimientoProducto(accion):
	if(accion=="1"):
		mantenimiento.productos.insertarDatos()
	elif(accion=="2"):
		print("actualiza")
	elif(accion=="3"):
		print("elimina")
	elif(accion=="4"):
		print("lista")

	
def OpcionesSistemas():
	print("****************************************");
	print("*************SISTEMA VENTAS*************");
	print("****************************************");
	print("MENU");
	print("1=> MANTENIMIENTO");
	print("2=> VENTAS");
	print("3=> REPORTES");
	print("****************************************");

def OpcionesMantenimiento():
	print("*************MANTENIMIENTO*************");
	print("A=> Productos");
	print("B=> Usuario");
	print("C=> Cliente");
	print("D=> Vendedor");
	print("****************************************");

def OpcionesOperaciones(subopcion):

	if(subopcion=="A"):
		nombre="PRODUCTOS"
	elif(subopcion=="B"):
		nombre="USUARIO"
	elif(subopcion=="C"):
		nombre="CLIENTE"
	elif(subopcion=="D"):
		nombre="VENDEDOR"

	print("*************MANT."+nombre+"************");
	print("1=> Registra");
	print("2=> Actualiza");
	print("3=> Elimina");
	print("4=> lista");
	print("****************************************");


Load()