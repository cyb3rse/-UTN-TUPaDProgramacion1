#punto uno:1) 
lista=[]

for num in range(1,101,1):
 if num % 4==0:
       lista.append(num)
 else:
     pass
print(lista)

# punto dos:2)
alr=[]
for i in range(1,9,1):
    ele=str(input("ingrese su elemento favorito:"))
    alr.append(ele)
print(f"su penultimo elemento es:{alr[-2]}")

#punto numero tres:3)
ame=[]

for i in range(0,3,1):
  
  truc=False
  while truc==False:
     palab=str(input("ingrese una letra:_"))
     if palab.isdigit():
          print("el elemento ingresado es un numero")
          print("ingrese un nuevo elemento")
          truc=False
     else:
         ame.append(palab)
         truc=True

print(ame)

#punto cuatro:4)

animales = ["perro", "gato", "conejo", "pez"]
animales[-2]="oso"
animales[-1]="loro"
print(animales)
        
#punto cinco:5) en la primera linea se la a asignado cinco numeros a la variable "numero"
# ya en la segunda linea utilia la funcion .remove a la variable numero para sacar el numero mas alto de la lista "numero"    
#señandalo con max(numero) y al final imprime la lista con print() mostrando los numeros ingresados
#ingresados en la primera linea pero sin el numero mas grande entre estos

#punto seis:6) 
numb=[]
for i in range(10,31,5):
    numb.append(i)
print(numb[0:2])

#punto siete:7)
autos = ["sedan", "polo", "suran", "gol"]

autos[1]="carlo"
autos[2]="menija"
print(autos)

#punto ocho:8)
dobles=[]
for i in range(5,16,5):
 if i==5:
     dobles.append(i+i)
 elif i==10:
     dobles.append(i+i)
 elif i==15:
     dobles.append(i+i)
print(dobles)

#punto nueve:9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]=("tallarines")
compras[0].pop(0)
print(compras)

#punto diez:10)
lista_anidada=[]
segunda_lista=[]
lista_anidada.append(15)
lista_anidada.append(True)
segunda_lista.append(25.5)
segunda_lista.append(57.9)
segunda_lista.append(30.6)
lista_anidada.append(segunda_lista)
lista_anidada.append(False)
print(lista_anidada)














