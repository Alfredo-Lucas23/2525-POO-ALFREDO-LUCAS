import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id].actualizar_precio(precio)

    def buscar_por_nombre(self, nombre):
        return [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_todos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: p.to_dict() for id, p in self.productos.items()}, f)

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                self.productos = {id: Producto.from_dict(p) for id, p in data.items()}
        except FileNotFoundError:
            self.productos = {}
