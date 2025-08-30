def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
            print("Producto añadido correctamente.")

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado correctamente.")

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no se actualiza): ")
            precio = input("Nuevo precio (dejar vacío si no se actualiza): ")
            inventario.actualizar_producto(
                id,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )
            print("Producto actualizado correctamente.")

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            print("Resultados:", resultados)

        elif opcion == "5":
            print("Inventario:")
            print(inventario.mostrar_todos())

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")
            print("Inventario guardado. Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
