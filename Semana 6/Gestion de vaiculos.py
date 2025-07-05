# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = 0  # Atributo encapsulado

    def acelerar(self):
        self._velocidad += 10
        print(f"{self.marca} {self.modelo} acelerando. Velocidad: {self._velocidad} km/h")

    def frenar(self):
        self._velocidad = max(0, self._velocidad - 10)
        print(f"{self.marca} {self.modelo} frenando. Velocidad: {self._velocidad} km/h")

    def mostrar_info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")


# Clase derivada: Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Polimorfismo: sobrescribimos el método mostrar_info
    def mostrar_info(self):
        print(f"Auto: {self.marca} {self.modelo}, Puertas: {self.puertas}")


# Clase derivada: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    # Polimorfismo: sobrescribimos el método mostrar_info
    def mostrar_info(self):
        print(f"Moto: {self.marca} {self.modelo}, Tipo: {self.tipo}")


# Crear instancias y demostrar funcionalidad
auto1 = Auto("Toyota", "Corolla", 4)
moto1 = Moto("Yamaha", "MT-07", "Deportiva")

# Uso de métodos
auto1.mostrar_info()
auto1.acelerar()
auto1.frenar()

print()

moto1.mostrar_info()
moto1.acelerar()
moto1.frenar()
