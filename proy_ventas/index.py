import mantenimiento.productos
def Load():
	MenuPrincipal()
	
	
def MenuPrincipal():
	print("****************************************")
	print("*************SISTEMA VENTAS*************")
	print("****************************************")
	print("MENU")
	print("A=> MANTENIMIENTO")
	print("B=> VENTAS")
	print("C=> REPORTES")
	print("****************************************")
	
	opcion=input("Ingrese una opción:")

	if(opcion=="A"):
		OpcionesMantenimiento()
	elif(opcion=="B"):
		print("Ventas")
	elif(opcion=="C"):
		print("Reportes")
	else:
		print("La opción: "+opcion+" ingresada no existe")

def OpcionesMantenimiento():
	print("*************MANTENIMIENTO*************")
	print("A=> Productos")
	print("B=> Usuario")
	print("C=> Cliente")
	print("D=> Vendedor")
	print("****************************************")
	opcion=input("Ingrese una opción:")

	if(opcion=="A"):
		OpcionesProductos()
	elif(opcion=="B"):
		print("usuarios")
	elif(opcion=="C"):
		print("cliente")
	elif(opcion=="D"):
		print("vendedor")
	else:
		print("La opción: "+opcion+" ingresada no existe")

def OpcionesProductos():
	print("*************MANT.PRODUCTOS************")
	print("A=> Registra")
	print("B=> Actualiza")
	print("C=> Elimina")
	print("D=> lista")
	print("****************************************")

	opcion=input("Ingrese una opción:")

	if(opcion=="A"):
		RegistarProducto()
	elif(opcion=="B"):
		print("usuarios")
	elif(opcion=="C"):
		print("cliente")
	elif(opcion=="D"):
		print("vendedor")
	else:
		print("La opción: "+opcion+" ingresada no existe")

def RegistarProducto():
	mantenimiento.productos.insertarDatos()
	
Load()