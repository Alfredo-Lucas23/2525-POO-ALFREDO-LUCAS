class Usuario:
    def __init__(self, jose, archivo_log):
        """
        Constructor de la clase Usuario.
        Se ejecuta automáticamente al crear una nueva instancia de Usuario.
        Inicializa el nombre del usuario y abre un archivo de log para registrar actividades.
        """
        self.nombre = jose
        self.archivo_log = open(archivo_log, 'a')
        self.archivo_log.write(f"[INFO] Usuario '{self.nombre}' ha iniciado sesión.\n")
        print(f"Bienvenido, {self.nombre}.")

    def realizar_accion(self, accion):
        """
        Simula una acción realizada por el usuario y la registra en el archivo de log.
        """
        self.archivo_log.write(f"[ACCION] {self.nombre} realizó: {accion}\n")
        print(f"{self.nombre} realizó la acción: {accion}")

    def __del__(self):
        """
        Destructor de la clase Usuario.
        Se ejecuta automáticamente cuando el objeto es destruido o el programa finaliza.
        Cierra el archivo de log y registra el cierre de sesión.
        """
        self.archivo_log.write(f"[INFO] Usuario '{self.nombre}' ha cerrado sesión.\n")
        self.archivo_log.close()
        print(f"Hasta luego, {self.nombre}. El archivo de log ha sido cerrado.")
