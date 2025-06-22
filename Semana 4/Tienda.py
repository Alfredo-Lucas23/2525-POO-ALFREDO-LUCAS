# tienda.py

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio:.2f}"


# Clase Cliente
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = []

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"{producto.nombre} agregado al carrito de {self.nombre}.")

    def mostrar_carrito(self):
        print(f"Carrito de {self.nombre}:")
        for producto in self.carrito:
            print(f" - {producto.mostrar_info()}")


# Clase Pedido
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = cliente.carrito
        self.total = sum(p.precio for p in self.productos)

    def resumen_pedido(self):
        print(f"Resumen del pedido para {self.cliente.nombre}:")
        for producto in self.productos:
            print(f" - {producto.mostrar_info()}")
        print(f"Total a pagar: ${self.total:.2f}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    p1 = Producto("Laptop", 1200.00)
    p2 = Producto("Mouse", 25.50)

    # Crear cliente
    cliente1 = Cliente("Ana", "ana@email.com")

    # Agregar productos al carrito
    cliente1.agregar_al_carrito(p1)
    cliente1.agregar_al_carrito(p2)

    # Mostrar carrito
    cliente1.mostrar_carrito()

    # Crear pedido
    pedido1 = Pedido(cliente1)
    pedido1.resumen_pedido()
