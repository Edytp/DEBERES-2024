import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

    def to_line(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_line(line):
        id_producto, nombre, cantidad, precio = line.strip().split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        producto = Producto.from_line(linea)
                        self.productos[producto.id_producto] = producto
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            # Crear archivo si no existe
            try:
                open(self.archivo, 'w').close()
            except PermissionError as e:
                print(f"Error al crear el archivo de inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(producto.to_line())
            print("Inventario guardado exitosamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)