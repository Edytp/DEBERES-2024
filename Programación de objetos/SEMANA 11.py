import json


# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Producto con este ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_cantidad(self, id_producto, cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].set_cantidad(cantidad)
            print("Cantidad actualizada.")
        else:
            print("Producto no encontrado.")

    def actualizar_precio(self, id_producto, precio):
        if id_producto in self.productos:
            self.productos[id_producto].set_precio(precio)
            print("Precio actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.get_nombre() == nombre]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("Producto no encontrado.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: producto.__dict__ for id, producto in self.productos.items()}, f)
        print("Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                self.productos = {id: Producto(**info) for id, info in data.items()}
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado.")


# Función de menú
def menu():
    print("\nSistema de Gestión de Inventario")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Cantidad")
    print("4. Actualizar Precio")
    print("5. Buscar Producto por Nombre")
    print("6. Mostrar Todos los Productos")
    print("7. Guardar Inventario en Archivo")
    print("8. Cargar Inventario desde Archivo")
    print("9. Salir")


# Función principal
def main():
    inventario = Inventario()
    archivo = 'inventario.json'

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar cantidad: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, cantidad)

        elif opcion == '4':
            id_producto = input("ID del producto a actualizar precio: ")
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id_producto, precio)

        elif opcion == '5':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '6':
            inventario.mostrar_todos_los_productos()

        elif opcion == '7':
            inventario.guardar_en_archivo(archivo)

        elif opcion == '8':
            inventario.cargar_desde_archivo(archivo)

        elif opcion == '9':
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == '__main__':
    main()