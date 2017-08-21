import mantenimiento.productos
import mantenimiento.usuario
import mantenimiento.cliente
import mantenimiento.vendedor

def load():
    menuPrincipal()

def menuPrincipal():
    print("****************************************")
    print("*************SISTEMA VENTAS*************")
    print("****************************************")
    print("MENU")
    print("A=> MANTENIMIENTO")
    print("B=> VENTAS")
    print("C=> REPORTES")
    print("****************************************")

    opcion = input("Ingrese una opción:")

    if opcion == "A":
        opcionesMantenimiento()
    elif opcion == "B":
        print("Ventas")
    elif opcion == "C":
        print("Reportes")
    else:
        print("La opción: " + opcion + " ingresada no existe")




def opcionesMantenimiento():
    print("*************MANTENIMIENTO*************")
    print("A=> Productos")
    print("B=> Usuario")
    print("C=> Cliente")
    print("D=> Vendedor")
    print("****************************************")
    opcion = input("Ingrese una opción:")

    if opcion == "A":
        opcionesProductos()
    elif opcion == "B":
        opcionesUsuarios()
    elif opcion == "C":
        opcionesClientes()
    elif opcion == "D":
        opcionesVendedores()
    else:
        print("La opción: " + opcion + " ingresada no existe")


# INICIO-REGIÓN MANTENIMIENTO DE PRODUCTOS
def opcionesProductos():
    print("*************MANT.PRODUCTOS************")
    print("A=> Registra")
    print("B=> Actualiza")
    print("C=> Elimina")
    print("D=> lista")
    print("****************************************")

    opcion = input("Ingrese una opción:")

    if opcion == "A":
        registarProducto()
    elif opcion == "B":
        actualizarProducto()
    elif opcion == "C":
        eliminarProducto()
    elif opcion == "D":
        listarProducto()
    else:
        print("La opción: " + opcion + " ingresada no existe")

def registarProducto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = input("Ingrese el precio del producto: ")

    mantenimiento.productos.insertarDatos(nombre_producto, precio_producto)

def actualizarProducto():
    id_producto = input("ingrese un id: ")
    nombre_producto = input("ingrese un nombre: ")

    mantenimiento.productos.actualizarDatos(id_producto, nombre_producto)

def eliminarProducto():
    id_producto = input("Ingrese id: ")
    mantenimiento.productos.eliminarDatos(id_producto)

def listarProducto():

    mantenimiento.productos.leerDatos()

# FIN-REGIÓN MANTENIMIENTO DE PRODUCTOS

# INICIO-REGIÓN MANTENIMIENTO DE PRODUCTOS


def opcionesUsuarios():
    print("*************MANT.USUARIOS************")
    print("A=> Registra")
    print("B=> Actualiza")
    print("C=> Elimina")
    print("D=> lista")
    print("****************************************")

    opcion = input("Ingrese una opción:")

    if opcion == "A":
        registarUsuario()
    elif opcion == "B":
        actualizarUsuario()
    elif opcion == "C":
        eliminarUsuario()
    elif opcion == "D":
        listarUsuario()
    else:
        print("La opción: " + opcion + " ingresada no existe")

def registarUsuario():
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    password_usuario = input("Ingrese el password del usuario: ")

    mantenimiento.usuario.insertarDatos(nombre_usuario, password_usuario)

def actualizarUsuario():
    id_usuario=input("Ingrese el id del usuario: ")
    nombre_usuario=input("Ingrese el nombre del usuario: ")

    mantenimiento.usuario.actualizarDatos(id_usuario,nombre_usuario)

def eliminarUsuario():
    id_usuario=input("Ingrese el id del usuario: ")

    mantenimiento.usuario.eliminarDatos(id_usuario)

def listarUsuario():
    mantenimiento.usuario.leerDatos()
# FIN-REGIÓN MANTENIMIENTO DE PRODUCTOS

#INICIO-REGIÓN VENDEDORES

def opcionesClientes():
    print("*************MANT.CLIENTES************")
    print("A=> Registra")
    print("B=> Actualiza")
    print("C=> Elimina")
    print("D=> lista")
    print("****************************************")

    opcion = input("Ingrese una opción:")

    if opcion == "A":
        registarCliente()
    elif opcion == "B":
        actualizarCliente()
    elif opcion == "C":
        eliminarCliente()
    elif opcion == "D":
        listarCliente()
    else:
        print("La opción: " + opcion + " ingresada no existe")

def registarCliente():
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        ruc_cliente = input("Ingrese el ruc del cliente: ")
        direccion_cliente = input("Ingrese la dirección del cliente: ")

        mantenimiento.cliente.insertarDatos(nombre_cliente,ruc_cliente,direccion_cliente)

def actualizarCliente():
        id_cliente = input("Ingrese el id del cliente: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        mantenimiento.cliente.actualizarDatos(id_cliente, nombre_cliente)

def eliminarCliente():
        id_cliente = input("Ingrese el id del cliente: ")

        mantenimiento.cliente.eliminarDatos(id_cliente)

def listarCliente():
        mantenimiento.cliente.leerDatos()

#FIN-REGIÓN CLIENTES

#INICIO-REGIÓN VENDEDORES
def opcionesVendedores():
    print("*************MANT.VENDEDORES************")
    print("A=> Registra")
    print("B=> Actualiza")
    print("C=> Elimina")
    print("D=> lista")
    print("****************************************")

    opcion = input("Ingrese una opción:")

    if opcion == "A":
        registarVendedor()
    elif opcion == "B":
        actualizarVendedor()
    elif opcion == "C":
        eliminarVendedor()
    elif opcion == "D":
        listarVendedor()
    else:
        print("La opción: " + opcion + " ingresada no existe")

def registarVendedor():
    nombre_vendedor = input("Ingrese el nombre del vendedor: ")

    mantenimiento.vendedor.insertarDatos(nombre_vendedor)

def actualizarVendedor():
    id_vendedor=input("Ingrese el id del vendedor: ")

    mantenimiento.vendedor.actualizarDatos(id_vendedor)

def eliminarVendedor():
    id_vendedor=input("Ingrese el id del vendedor: ")

    mantenimiento.vendedor.eliminarDatos(id_vendedor)

def listarVendedor():
    mantenimiento.vendedor.leerDatos()

#FIN-REGIÓN VENDEDORES
load()
