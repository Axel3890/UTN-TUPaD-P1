##1) Factorial recursivo y mostrar todos los factoriales hasta un número dado
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

limite = int(input("Ingresa un número entero positivo: "))
print("Factoriales desde 1 hasta", limite)
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

##2) Fibonacci recursivo y mostrar la serie hasta una posición dada
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingresa una posición para la serie de Fibonacci: "))
print("Serie de Fibonacci hasta la posición", pos)
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")

##3) Potencia recursiva

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")



##4) Conversión recursiva de decimal a binario

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("Ingresa un número entero positivo: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")

##5) Función recursiva es_palindromo(palabra)
def es_palindromo(palabra):

    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


print(es_palindromo("reconocer")) 
print(es_palindromo("python"))    
print(es_palindromo("neuquen"))   
print(es_palindromo("radar"))      

##6) Función recursiva suma_digitos(n) sin convertir a string
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


print(suma_digitos(1234))  
print(suma_digitos(9))    
print(suma_digitos(305))  

##7) Función recursiva contar_bloques(n)
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


print(contar_bloques(1))  
print(contar_bloques(2))  
print(contar_bloques(4))  
print(contar_bloques(5)) 

##8) Función recursiva contar_digito(numero, digito)
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    contador = 1 if ultimo == digito else 0
    return contador + contar_digito(numero // 10, digito)

# Ejemplos
print(contar_digito(12233421, 2))  # → 3
print(contar_digito(5555, 5))      # → 4
print(contar_digito(123456, 7))    # → 0
