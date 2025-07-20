import os

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo Python dado su path absoluto.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """
    Muestra un menú interactivo para acceder a scripts organizados por unidad y tema.
    """
    ruta_base = os.getcwd()  # Usa el directorio actual

    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 2/2.1. Clases y Objetos/2.1.1. Ejemplo Clases.py',
        '3': 'UNIDAD 3/3.1. Herencia/3.1.1. Ejemplo Herencia.py',
        '4': 'UNIDAD 4/4.1. Polimorfismo/4.1.1. Ejemplo Polimorfismo.py',
        '5': 'UNIDAD 5/5.1. Proyecto Final/5.1.1. Proyecto.py'
    }

    while True:
        print("\n📌 Menú Principal - Dashboard de Programación Orientada a Objetos")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del dashboard. ¡Hasta luego!")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
