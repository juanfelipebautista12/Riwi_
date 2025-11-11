#taller python

        #1

# print("hola usuario")
# nombre= input("cual es tu nombre?: ")
# edad= int(input("cual es tu edad actual?: "))
# print(f"hola {nombre}, tienes {edad} años")

        #2

# print("bienvenido a esta sencilla pero efectiva calculadora")

# numero1= int(input("ingresa el valor del numero 1: "))
# numero2= int(input("ingresa el valor del numero 2: "))

# resultado= numero1 + numero2
# print(" el resultado de la suma anterior es",resultado)

        #3

# print("bienvenido a el calculador de areas")

# base= int(input("ingresa el valor de la base del triangulo: "))
# altura= int(input("ingresa el valor de la altura del triangulo: "))

# resultado = base*altura//2
# print("el area del anterior triangulo es de", resultado)

        #4

# print("bienvenido a el conversor de grados celsius a farenheit")

# celsius= int(input("ingresa la cantidad de grados celsius: "))

# farenheit= (celsius*9//5) +32

# print("la cantidad de grados farenheit es de", farenheit , "°F" )

        #5

# opcion1= "hola mundo"
# opcion2= 3
# opcion3= 3.3

# variables= input("quieres saber que tipo de dato son las anteriores variables?(si/no): ")
# if variables== "no":
#         print("ok no me importa") 

# print(type(opcion1))   
# print(type(opcion2))
# print(type(opcion3))

        #6

# print("a continuacion te dire cuantos años tendras en 10 años")

# edad= int(input("ingresa tu edad actual: "))
# edaden10años= edad + 10 
# resultado= edaden10años 
# print(f"tu edad en 10 años seran: {resultado} años")

        #7

# print("a continuacion te dire si eres mayor de edad o no")

# edad= int(input("ingresa tu edad actual: "))

# if edad>= 18:
#     print("eres mayor de edad")

# elif edad<18:
#     print("lo siento no eres mayor de edad")

        #8

# print("detector de numeros")

# numero= int(input("ingresa un numero: "))

# if numero== 0:
#     print("es el cero")

# elif numero> 0:
#     print("el numero es positivo")

# elif numero< 0:
#     print("el numero es negativo")

        #9

# print("detector de numeros pares o impares")

# numero= int(input("ingresa un numero: "))
# if numero %2 == 0:
#     print("el numero es par")
# else:
#     print("el numero es impar")

        #10

print("bienvenido a esta calculadora basica")
print("puedes sumar, restar , multiplicar y dividir numeros enteros ")

numero1=int(input("ingresa el numero 1: "))
numero2=int(input("ingresa el numero 2: "))
operacion=input("que tipo de operacion quieres hacer? ")

suma= "+"
resta= "-"
multiplicacion= "*"
division= "//"
    
if operacion==suma: 
    resultado= numero1 + numero2
    print(f"el resultado es {resultado}")

elif operacion== resta:
        resultado1= numero1 - numero2
        print(f"el resultado es {resultado1}")

elif operacion==multiplicacion:
      resultado2= numero1 * numero2
      print(f"el resultado es {resultado2}")

elif operacion== division:
        
        if numero2 == 0:
               print("no se puede dividir por cero")

        else: 
                resultado3 = numero1 // numero2
                print(f"el resultado es {resultado3}") 










 











