print("🔥 Bienvenido al inventario del supermercado la madera 🔥")

validacion= input("Quieres ingresar informacion a tu inventario?(si/no): ")

while validacion.lower() == "si":
    

    #validacion del nombre del producto:
    while True:
        nombre= input("ingrese el nombre del producto a registrar: ")
        if nombre.isnumeric() or nombre== "" :
            print("❌ ingresa un nombre valido por favor ❌")

        else:
            break 

    #validacion del precio de cada unidad:
    while True:
        try:
            precio= float(input("ingresa el precio de cada unidad: "))
            if precio < 0:
                print("el precio no puede ser negativo")
            else:
                break
        except ValueError:
            print("❌ ingrese un valor valido por favor ❌")

    #validacion de cantidad de unidades:
    while True:
        try:
            cantidad= int(input("ingresa la cantidad de unidades: "))
            if cantidad <= 0:
                print("❌ ingresa una cantidad valida por favor ❌")
            else:
                break
        except ValueError:
            print("❌ ingresa un numero valido para la cantidad ❌")

    print("\n✅ producto registrado correctamente ✅")
    print(f"registraste: {nombre}")
    print(f"precio/unidad: ${precio:.3f}")
    print(f"cantidad: {cantidad}")
    total= precio*cantidad
    print(f"el total precio/cantidad es: {total:.3f}")

    validacion= input("quieres ingresar otro producto?(si/no): ")

print("\n❤️ gracias por preferir nuestro programa de inventario ❤️")
