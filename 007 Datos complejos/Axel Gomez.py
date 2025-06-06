# 1: Añadir frutas al diccionario

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2: Actualizar precios

# Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3: Crear lista con solo las frutas

# Obtener solo las frutas (claves del diccionario)
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)


# 3: Crear lista con solo las frutas


# Obtener solo las frutas (claves del diccionario)
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)


# 4: Agenda telefónica
# Crear diccionario de contactos
agenda = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = telefono

# Consultar un contacto
consulta = input("Ingresá el nombre del contacto que querés buscar: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")


# 5: Frase del usuario, palabras únicas y recuento
    # Solicitar frase
frase = input("Ingresá una frase: ")

# Separar palabras
palabras = frase.lower().split()

# Palabras únicas
palabras_unicas = set(palabras)

# Recuento de cada palabra
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)


# 6: Notas de alumnos y promedio
# Crear diccionario de alumnos con tuplas de notas
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")


# 7: Operaciones con sets de estudiantes
    # Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "Pedro", "Lucía", "Marta"}
parcial2 = {"Pedro", "Marta", "Sofía", "Juan"}

# Estudiantes que aprobaron ambos parciales
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno de los dos parciales
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos uno (sin repetir)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


# 8: Gestión de stock de productos

# Diccionario de productos con stock inicial
stock = {
    "arroz": 10,
    "fideos": 20,
    "azúcar": 15
}

# Consulta o actualización de stock
producto = input("Ingresá el nombre de un producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("¿Querés agregar unidades a este producto? (s/n): ").lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    agregar_nuevo = input(f"{producto} no está en stock. ¿Querés agregarlo? (s/n): ").lower()
    if agregar_nuevo == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] = unidades
        print(f"Producto {producto} agregado con stock de {unidades} unidades.")
    else:
        print("No se agregó el producto.")

# 9: Agenda con claves como tuplas

# Agenda con tuplas como claves
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio"
}

# Consulta al usuario
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

# Buscar la actividad
clave = (dia, hora)
if clave in agenda:
    print(f"Actividad en {dia} a las {hora}: {agenda[clave]}")
else:
    print("No hay actividad programada en ese día y hora.")

# 10: Invertir diccionario (capitales como claves)

# Diccionario original: país -> capital
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Invertir el diccionario: capital -> país
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar el resultado
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)