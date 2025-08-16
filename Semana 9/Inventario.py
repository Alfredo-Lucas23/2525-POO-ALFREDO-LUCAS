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

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(" Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print(" Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑 Producto eliminado.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(" Producto actualizado.")
                return
        print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print(" Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print(" Inventario completo:")
            for p in self.productos:
                print(p)


# Menú interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
            precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print(" Opción inválida. Intente nuevamente.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
