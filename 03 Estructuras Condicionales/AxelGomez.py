import random
from statistics import mean, median, mode
# 1) Mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Aprobado o desaprobado
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Número par
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Categorías por edad
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Validar contraseña por longitud
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostrar valores
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinar sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("Distribución con sesgo no definido claramente")

# 7) Verificar si la frase termina en vocal
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"

if frase[-1] in vocales:
    frase += "!"
    
print("Resultado:", frase)

# 8) Transformar el nombre según elección
nombre = input("Ingrese su nombre: ")

print("Opciones:")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Primera letra en mayúscula")

opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida")

    # 9) Clasificación de terremoto según la escala de Richter
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# 10) Determinar estación según hemisferio y fecha
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

# Convertir fecha a un número para facilitar comparación: MMDD (ej: 3 de abril => 403)
fecha = mes * 100 + dia

# Definir las estaciones por rangos de fechas
if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif 321 <= fecha <= 620:
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif 621 <= fecha <= 920:
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif 921 <= fecha <= 1220:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Fecha inválida"

# Mostrar estación según hemisferio
if hemisferio == "N":
    print(f"En el hemisferio norte, la estación actual es: {estacion_norte}")
elif hemisferio == "S":
    print(f"En el hemisferio sur, la estación actual es: {estacion_sur}")
else:
    print("Hemisferio no válido. Use 'N' para norte o 'S' para sur.")


