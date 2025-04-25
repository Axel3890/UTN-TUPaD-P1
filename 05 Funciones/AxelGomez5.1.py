# Actividad 1
def obtener_multiplos_de_4():
    multiplos = list(range(4, 101, 4))
    print("Múltiplos de 4 del 1 al 100:", multiplos)

# Actividad 2
def mostrar_penultimo_elemento():
    favoritos = ["pizza", "música", "videojuegos", "leer", "viajar"]
    print("Penúltimo elemento:", favoritos[-2])

# Actividad 3
def crear_lista_con_append():
    lista = []
    lista.append("sol")
    lista.append("luna")
    lista.append("estrella")
    print("Lista con palabras agregadas:", lista)

# Actividad 4
def modificar_lista_animales():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print("Lista modificada de animales:", animales)

#Actividad 5
#Se presenta una lista de números. Luego se elimina el valor más alto de la lista utilizando max() para obtenerlo y remove() para eliminarlo. 
# El resultado final es la lista sin ese valor máximo.


# Actividad 6
def lista_saltos_de_5():
    numeros = list(range(10, 31, 5))
    print("Primeros dos elementos:", numeros[:2])

# Actividad 7
def reemplazar_autos():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["fiat", "civic"] 
    print("Lista de autos modificada:", autos)

# Actividad 8
def crear_lista_dobles():
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print("Lista de dobles:", dobles)

# Actividad 9
def modificar_compras():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")                # a) Agregar "jugo" al tercer cliente
    compras[1][1] = "tallarines"             # b) Reemplazar "fideos"
    compras[0].remove("pan")                 # c) Eliminar "pan"
    print("Lista de compras modificada:", compras)

# Actividad 10
def crear_lista_anidada():
    lista_anidada = [
        15,                   
        True,                 
        [25.5, 57.9, 30.6],   
        False                 
    ]
    print("Lista anidada:", lista_anidada)


obtener_multiplos_de_4()
mostrar_penultimo_elemento()
crear_lista_con_append()
modificar_lista_animales()
lista_saltos_de_5()
reemplazar_autos()
crear_lista_dobles()
modificar_compras()
crear_lista_anidada()
