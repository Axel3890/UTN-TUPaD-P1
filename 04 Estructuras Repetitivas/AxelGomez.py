import random
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
numero = input("Ingresa un número entero: ")
cantidad_digitos = len(numero.lstrip('-'))  # Elimina el signo negativo si existe
print(f"El número tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

menor = min(inicio, fin)
mayor = max(inicio, fin)

suma = sum(range(menor + 1, mayor))
print(f"La suma de los números entre {menor} y {mayor} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
total = 0

while True:
    numero = int(input("Ingresa un número entero (0 para finalizar): "))
    if numero == 0:
        break
    total += numero

print(f"La suma total es: {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
numero_secreto = random.randint(0, 9)
intentos = 0

print("Adivina el número entre 0 y 9")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")
        break
    else:
        print("Incorrecto, intenta de nuevo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero = int(input("Ingresa un número entero positivo: "))

if numero >= 0:
    suma = sum(range(numero + 1))
    print(f"La suma de los números entre 0 y {numero} es: {suma}")
else:
    print("El número debe ser positivo.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cantidad = 100 
pares = impares = positivos = negativos = 0

for i in range(cantidad):
    num = int(input(f"Ingreso {i+1}/{cantidad}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input(f"Ingreso {i+1}/{cantidad}: "))
    suma += num

media = suma / cantidad
print(f"La media de los {cantidad} números es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = input("Ingresa un número entero: ")

if numero.startswith('-'):
    invertido = '-' + numero[:0:-1]
else:
    invertido = numero[::-1]

print(f"El número invertido es: {invertido}")
