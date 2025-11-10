print("Bienvenido al inventario del supermercado la madera")

validacion= input("Quieres ingresar informacion a tu inventario?(si/no): ")

while validacion.lower() == "si":
    

    #validacion del nombre del producto
    while True:
        nombre= input("ingrese el nombre del producto a ingresar")
        if nombre.isnumeric() or nombre== "" :
            print("ingresa un nombre valido por favor")
            


