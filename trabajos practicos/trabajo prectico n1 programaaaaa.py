
helloo="hola mundo!"
print(helloo)


ses="hola "
sas=input("ingrese su nombre:")
print(ses+sas)

ses=input("ingrese su edad:")
sas=input("ingrese su nombre:")
lol=input("ingrese su apellido:")
lel=input("ingrese su lugar de residencia:")

resu=str(f"Soy {sas} {lol}, tengo  {ses}  a�os y vivo en {lel}")
print(resu)


perimetro=0
area=0
pi=3.14
radio=float(input("ingrese el radio de un circulo para calcular el area y su perimetro:"))
area=pi*(radio**2)
print(f"el area es: {area}")
perimetro=2+pi+radio
print(f"el perimetro es de: {perimetro}")




minu=0
seg=int(input("ingrese los segundos que quiera para saber cuanto es horas:"))
minu=int(seg/60)
horas=float(minu/60)
print(f"sus segundo a horas son: {horas}")

num1=10
tabla=int(input("ingrese un numero para saber su tabla:"))
print(f"la tabla del {tabla} es: ")
while num1 != 0:
    print(tabla*num1)
    num1=num1-1



num1=int(input("ingrese un numero que no sea 0 para sumarlo,restarlo,multiplicarlo y divirlo:"))
num2=int(input("ingrese otro numero:"))
suma=num1+num2
resta=num1-num2
multi=num1*num2
divi=float(num1/num2)
print(f"el resulado de la suma de {num1}+{num2} es: {suma}")
print(f"el resulado de la resta de {num1}-{num2} es: {resta}")
print(f"el resulado de la multiplicacion de {num1}*{num2} es: {multi}")
print(f"el resulado de la division de {num1}/{num2} es: {divi}")

 
peso=float(input("ingrese su peso para medir su masa moscular:"))
altu=float(input("ingrese su altura para medir su masa moscular:"))
altu=float(altu*altu)
masam=float(peso/altu)
print(f"su masa moscular es de: {masam}")

cal=int(input("ingrese un grado celsius para saber cuanto es en grados fahrenheit:"))
num1=cal*9/5
fal=num1+32
print(f"su grado celsius de: {cal} es: {fal} en grados fahrenheit")


num1=int(input("ingrese un numero para saber su promedio:"))
num2=int(input("ingrese un numero para saber su promedio:"))
num3=int(input("ingrese un numero para saber su promedio:"))
resu=float(num1+num2+num3)/3
print(f"el promedio de los numeros: {num1},{num2},{num3} es:{resu}")

