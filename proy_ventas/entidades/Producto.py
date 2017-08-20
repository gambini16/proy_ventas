class Producto(object):
	def __init__(self,id_producto,nombre_producto,precio_producto,estado_producto):
		self.id_producto=id_producto
		self.nombre_producto=nombre_producto
		self.precio_producto=precio_producto
		self.estado_producto=estado_producto

	def darId_producto(self):
		return self.id_producto
	def darNombre_producto(self):
		return self.nombre_producto
	def darPrecio_producto(self):
		return self.precio_producto
	def darEstado_producto(self):
		return self.estado_producto
	