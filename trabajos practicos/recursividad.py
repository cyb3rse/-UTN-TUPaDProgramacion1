#punto 1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num =int(input("Ingresa un número para ver cual es su factorial: "))
for i in range(1, num + 1):
    print(f"el factorial de {i} es {factorial(i)}")

#punto 2):
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

num = int(input("Ingresa un numero para ver su  serie de Fibonacci: "))
print(f"Serie de Fibonacci hasta la posición {num}:")
for i in range(num + 1):
    print(fibo(i))
#punto 3):

def potencia(base, expo):
    if expo == 0:
        return 1
    else:
        return base * potencia(base, expo - 1)

base = int(input("Ingresa la base: "))
expo= int(input("Ingresa el exponente para el numero: "))
res = potencia(base, expo)
print(f"{base} elevado a la {expo} es {res}")
#punto 4);
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("ingrese un numero: "))
bi = decimal_a_binario(num)
print(f"el nnmero {num} en binario es: {bi}")
#PPUNTO 5)
def es_palindromo(palabriña):
    if len(palabriña) <= 1:
        return True

    if palabriña[0] != palabriña[-1]:
        return False
        
    return es_palindromo(palabriña[1:-1])
    
palabriña = input("Ingresa una palabra sin espacios ni tildes porfis: ").lower()

if es_palindromo(palabriña):
    print("Es un palindromo: True.")
else:
    print("No es un palindromo: False")

#PUNTO 6)
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("ingresa un numero entero positivo: "))
resultado = suma_digitos(num)
print(f"la suma de los numeros de {num} es {resultado}")
#punto 7)
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("ingresa la cantidad de bloques del nivel mas bajo: "))
total = contar_bloques(nivel)
print(f"se necesitan {total} bloques para construir la piramide.")
#punto 80000000000)
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

num = int(input("ingresa un numero entero positivo: "))
dig = int(input("ingresa un digito entre 0 y 9 para ver si se encuentra: "))
resu = contar_digito(num, dig)
print(f"el igito {dig} aparece {resu} veces en el numero {num}.")
















