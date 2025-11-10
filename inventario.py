print("Bienvenido al supermercado la 2000")                               

usuario = input("¿Quieres ingresar un producto? (si/no): ")

while usuario.lower() == "si":
    

     # Validar nombre
    while True:
    
        nombre = input("Ingrese el nombre del producto: ")

        if nombre.isnumeric() or nombre == "" :
            print("nombre invalido deben ser letras... vuelve a intentarlo")
            
        else:
            break
            
# Validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("⚠️ El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("❌ Ingrese un valor válido para el precio.")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("⚠️ La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("❌ Ingrese un número entero válido para la cantidad.")

    print("\n✅ Producto registrado correctamente:")
    print(f"Nombre: {nombre}")
    print(f"Precio: ${precio:.3f}")
    print(f"Cantidad: {cantidad}\n")
    total= precio*cantidad
    print(f"el total de tu compra fue {total:.3f}")

    usuario = input("¿Quieres ingresar otro producto? (si/no): ")

print("Gracias por usar el sistema del supermercado la 2000 🛒") 





