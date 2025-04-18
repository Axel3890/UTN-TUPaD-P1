# 1. Función que imprime "Hola Mundo!" por pantalla
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que recibe un nombre y devuelve un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que recibe nombre, apellido, edad y residencia, y muestra la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

import math

# 4. Función que calcula el área de un círculo dado su radio
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# 4. Función que calcula el perímetro de un círculo dado su radio
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar de un número del 1 al 10
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que realiza operaciones básicas entre dos números y devuelve una tupla con los resultados
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# 8. Función que calcula el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Función que convierte grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":

    imprimir_hola_mundo()


    nombre_usuario = input("Ingresá tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)


    nombre = input("Ingresá tu nombre: ")
    apellido = input("Ingresá tu apellido: ")
    edad = input("Ingresá tu edad: ")
    residencia = input("Ingresá tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)


    radio = float(input("\nIngresá el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


    segundos = int(input("\nIngresá la cantidad de segundos: "))
    print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f} horas")


    numero_tabla = int(input("\nIngresá un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)

 
    a = float(input("\nIngresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")


    peso = float(input("\nIngresá tu peso en kg: "))
    altura = float(input("Ingresá tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")


    celsius = float(input("\nIngresá la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"Equivalente en Fahrenheit: {fahrenheit:.2f}°F")


    n1 = float(input("\nIngresá el primer número: "))
    n2 = float(input("Ingresá el segundo número: "))
    n3 = float(input("Ingresá el tercer número: "))
    promedio = calcular_promedio(n1, n2, n3)
    print(f"El promedio es: {promedio:.2f}")
