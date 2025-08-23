def agregar_contenido(nombre_archivo, texto):
    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write(texto + "\n")
        print("Contenido agregado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Crear el archivo con contenido inicial
with open("archivo_alternativo.txt", "w") as archivo:
    archivo.write("Contenido inicial del archivo.\n")

# Usar la función para agregar contenido al final
agregar_contenido("archivo_alternativo.txt", "Este es el nuevo contenido agregado al final.")
