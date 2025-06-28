# Programa para calcular el área de un triángulo
# El usuario ingresa la base y la altura, y el programa calcula el área usando la fórmula: (base * altura) / 2

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dados la base y la altura.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    area = (base * altura) / 2
    return area


# Solicitar datos al usuario
base_input = float(input("Ingresa la base del triángulo (en cm): "))
altura_input = float(input("Ingresa la altura del triángulo (en cm): "))

# Calcular el área
area_resultado = calcular_area_triangulo(base_input, altura_input)

# Mostrar el resultado
print(f"El área del triángulo es: {area_resultado} cm²")

# Verificación booleana (opcional)
es_area_positiva = area_resultado > 0
print(f"¿El área calculada es positiva? {es_area_positiva}")
