#punto 1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.
def imprime_hola_mundo():
 return"hola mundo!"

print(imprime_hola_mundo())
#punto 2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
  return(f"hola {nombre}")

nombre=str(input("ingrese su nombre:"))
print(saludar_usuario(nombre))

#punto 3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados.

def informacion_personal(nombre, apellido, edad, residencia):
 return(f"soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}")
   
   
print("presentacion PERSONALIZADA!!!!")
nombre=str(input("ingrese su nombre para la presentacion PERSONALIZADA:_"))
apellido=str(input("ingrese su apellido para la presentacion PERSONALIZADA:_"))
edad=str(input("ingrese su edad para la presentacion PERSONALIZADA:_"))
residencia=str(input("ingrese su residencia para la presentacion PERSONALIZADA:_"))
print("----------------------------------------------------------------")
print(informacion_personal(nombre, apellido, edad, residencia))
 
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuelva el 
#perímetro del círculo. Solicitar el radio al usuario y llamar ambas
#funciones para mostrar los resultados.

def calcular_area_circulo(radio):
  return(3.14*radio**2)
def calcular_perimetro_circulo(radio):
  return(2*3.14*radio)

validador=False

while validador==False:
 radio=str(input("ingrese el redio de un circulo para saber su area y perimetro"))
 if radio.isdigit():
    radio=float(radio)
    validador=True
 else:
    print("a ingresado datos incorrectos intentelo devuelva:")
    validador=False

print("el area del circulo es de:")   
print(calcular_area_circulo(radio))
print("y su perimetro de:")
print(calcular_perimetro_circulo(radio))
  
#punto 5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado
#usando esta función.

def segundos_a_horas(segundos):
 return(segundos/3600)
 
print("SEGUNDOS A HORAS!!!")
validacion=False
while validacion==False:
 print("ingrese sus segundos para pasarlos a horas__")
 segundos=str(input("__"))
 if segundos.isdigit():
   segundos=float(segundos)
   validacion=True
 else:
    print("a ingresado un caracter no solicitado intentelo nuevamente:_")
    print("------------------------------------------------------")

print(f"los segundos: {segundos} a horas son:")
print(segundos_a_horas(segundos))

#punto 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero,i):
  return(numero*i)

print("TABLAS")
confirmacion=False
while confirmacion==False:
  print("ingrese el numero del cual quiere ver la tabla:__")
  numero=str(input("__"))
  if numero.isdigit():
    numero=int(numero)
    confirmacion=True
  else:
    print("usted a ingresado un valor incorrecto,intento de nuevo")
     
for i in range(1,11):    
 print(f"la tabla del {numero}x{i} es:")
 print(tabla_multiplicar(numero,i))
 
#punto  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
 if a>b :
     return(f"la resta {a}-{b} es:", a-b,f" la suma de {a}+{b} es:", a+b, f"  la multiplicacion de {a}x{b} es:", a*b,f" la division de {a}/{b} es:", a/b)
 else:
     return(f"la resta {a}-{b} es:", b-a,f" la suma de {a}+{b} es:", a+b, f"  la multiplicacion de {a}x{b} es:", a*b,f" la division de {a}/{b} es:", b/a)

confirmacion=False
while confirmacion==False:
  num1=str(input("ingrese un numero:_"))
  num2=str(input("ingrese otro numero:_"))
  if num1.isdigit() and num2.isdigit():
    num1=int(num1)
    num2=int(num2)
    confirmacion=True
  else:
    print("usted a ingresado un valor incorrecto,intento de nuevo")

print(operaciones_basicas(num1,num2))

#punto 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#  para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    return round(imc,3)
    
confirmacion=False
while confirmacion==False:
  altura=str(input("ingrese su altura en metros para medir la masa corporal:_"))
  peso=str(input("ahora ingrese su peso en kilogramos:_"))
  
  if altura.replace(".","",1).isdigit() and peso.replace(".","",1).isdigit():
    altura=float(altura)
    peso=float(peso)
    confirmacion=True
  else:
    print("usted a ingresado un valor incorrecto,intento de nuevo")
    
masa_corporal=(calcular_imc(peso,altura))
print(f"su masa corporal es de:{calcular_imc(peso,altura)} eso indica que es:")

if masa_corporal< 18.5:
 print("su peso es Bajo")
elif masa_corporal<25.0:
 print("su peso es normal")
elif masa_corporal<30.0:
 print("usted tiene Sobrepeso")
elif masa_corporal <35.0:
 print("usted presenta obesidad(I)")
elif masa_corporal <40.0:
 print("usted tiene Obesidad(II)")
elif masa_corporal>39.9 :    
 print("usted tiene Obesidad(III)")

#punto 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
 Fahrenheit=(grados_cel*1.8)+32
 return round(Fahrenheit,1)
confirmacion=False
while confirmacion==False:
  grados_cel=str(input("ingrese su altura en metros para medir la masa corporal:_"))
  
  if grados_cel.isdigit():
    grados_cel=int(grados_cel)
    confirmacion=True
  else:
    print("usted a ingresado un valor incorrecto,intento de nuevo")
 
print("sus grados celsius a Fahrenheit es: ")
print(celsius_a_fahrenheit(grados_cel))

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
 resu=(a+b+c)/3
 return resu
 
confirmacion=False
while confirmacion==False:
  alvin=str(input("ingrese un numero solo se pertimen enteros:_"))
  biktor=str(input("ingrese otro numero:__"))
  carlos=str(input("ingrese su ultimo numero:__"))
  
  if alvin.isdigit() and biktor.isdigit() and carlos.isdigit():
    print(f"el promedio de los numeros {alvin},{biktor},{carlos} es de:_")
    alvin=float(alvin)
    biktor=float(biktor)
    carlos=float(carlos)
    confirmacion=True
  else:
    print("usted a ingresado un valor incorrecto,intento de nuevo")

print(calcular_promedio(alvin,biktor,carlos))