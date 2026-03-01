def calculator():
    while True:
        print(""" *****Porfavor seleccione una opcion valida***
        a. suma
        b. resta
        c. multiplicacion
        d. division
        e. salir
        """)

        opcion = input("Ingrese la operación a ejecutar: ").lower().strip()

        if opcion == "e" or opcion == "salir":
            print("*** Saliendo del programa ***")
            break

        if opcion not in ["a", "b", "c", "d", "suma", "resta", "multiplicacion", "division"]:
            print("Opción no válida. Intente de nuevo.")
            continue

        try:
            a = float(input("Ingrese el valor a: "))
            b = float(input("Ingrese el valor b: "))
        except ValueError:
            print("Error: Debe ingresar números válidos")
            continue

        if opcion in ["a", "suma"]:
            print(f"El resultado es: {a + b}")
        elif opcion in ["b", "resta"]:
            print(f"El resultado es: {a - b}")
        elif opcion in ["c", "multiplicacion"]:
            print(f"El resultado es: {a * b}")
        elif opcion in ["d", "division"]:
            if b != 0:
                print(f"El resultado es: {a / b}")
            else:
                print("Error: División por cero no permitida")


calculator()
