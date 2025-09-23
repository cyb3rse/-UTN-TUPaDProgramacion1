#punto uno)
num=0
for num in range(0,101):  
  print(num)

#punto dos
num1=input("ingrese un numero para saber su cantidad de digitos:")
num2=len(num1) 
if num1.isdigit():
   num3=True
else:
   num3=False

while num3==False:
   print("en elemento ingresado no es el solicitado")
   print("porfavor ingreselo devuelta")
   print("-----------------------------------------------------------")
   num1=input("ingrese un numero para saber su cantidad de digitos:")
   num2=len(num1) 
   if num1.isdigit():
     num3=True
   else:
     num3=False

print(num2)
#punto tres

numb1=int(input("ingrese un valor para saber la suma de sus enteros comprendidos:"))
numb2=int(input("ingrese un valor mas:"))
print("----------------------------------------------------------------")

resu=(0)
numb1=int(numb1-1)
numb2=int(numb2-1)
if numb1> numb2:
   
  for numb1 in range(numb1,numb2,-1):
      print(numb1)
      resu=numb1+resu
elif numb1<numb2:

  for numb2 in range(numb2,numb1,-1):
     print(numb2)
     resu=numb2+resu
elif numb1==numb2:
    print("el resultado es iguala a:0")

if numb1> numb2:
   resu=resu-numb2
elif numb1<numb2:
   resu=resu-numb1

print(resu-1)

#punto cuatro 4) 
recopi=int(0)
forreal=False
while forreal==False:
    numbin=int(input("ingrese su numero:"))    
    recopi=numbin+recopi
    mandarina=False
    while mandarina==False:
      print("quieres sumar otro numero?")
      quiere=int(input("ingese     /0=no/ o /1=si/    dependiendo de lo que quiera"))
      nos=0
      sis=1
      if quiere== nos:
          forreal=True
          mandarina=True
      elif quiere==sis:
           forreal=False
           mandarina=True
      else:
        print("el comando ingresado no es el correcto")
        print("porfavor ingrese los datos solicitados")
        forreal=False
        mandarina=False
print(f"esta es la cantidad total de todos los numeros sumado:{recopi}")

#punto cinco:5)

print("JUEGO DE ADIVINANZAS")
print("-----")

empezar=False
frase1=("cercaaaa","sos muy malo adivinando che")
conta=1
while empezar==False:
    print("apriete /1:para comenzar   /0:para salir del juego")
    star=int(input("º_º--?:"))

    if star==1:
      print("reglas:tiene que adivinar un numero aletorio entre 0 y 9 con los menos intentos posibles")
      print("-----------------------------------------------------------")
      import random
      numba=random.randint(0,9)
      arina=int(input("ya se han generado el numero aletorio adivina cual es:"))
      if arina!=numba:
            while arina!=numba:
             fraseale=random.choice(frase1)
             print("incorectoooo")
             print(fraseale)
             conta=conta+1
             empezar=True
             print("----------------------------------------------------------------")
             arina=int(input("intentelo denuevo 0u0:"))

            print(f"los intentos que le tomo para divinarlo son:{conta}")
            print("mejor suerte la proxima lel")
      elif arina==numba:
          print("correcto adivinado al primr intento increible 0_0_-")
    elif star==0:
       empezar=True
    else:
     print("el comando introducido no se encuentra disponible")
     print("ingrese un de los dos comandos dichos")
     empezar=False
#punto seis:6)

for conta in range(101,0,-1):
      if conta % 2==0:
         print(conta)
#punto siete:7)
     
sas=False
sumare=0
while sas==False:    
  
  try:
       lel=int(input("ingrese un numero arriba de cero para sumar sus numeros comprendidos desde el 0:"))
       print("----------------------------------------------------------------------------------")
  
       if lel>0: 
            for lel in range(lel,0,-1):
                sumare=lel+sumare
                sas=True
       elif lel<=0:
            print
            print("el comando ingresado no es el solicitado porfavor ingreselo nuevamente:")
            print("---------------------------------------------------")
            sas=False
  except ValueError:
        print("---------------------------------------------------------------")
        print("el comando ingresado es incorecto porfavor ingrese una variable numerica:")
        print("---------------------------------------------------")
        sas=False

print(f"la suma de los numero entre 0 y {lel} es: {sumare}")
#punto ocho:8) 

for mario in range(100,0,-1):
    luigi=False
    while luigi==False:
        try:
            print("ingrese un numero para clasificarlo:")
            nume=int(input("_"))
            if nume>=0 and nume % 2==0:
             print(f"el valor:{nume} es par y positivo")
             luigi=True
             par=par+1
             positivos=positivos+1
            elif nume>=0 and nume % 2!=0:
                print(f"el valor:{nume} es inpar y positivo")
                luigi=True
                inpar=inpar+1
                positivos=positivos+1
            elif nume<0 and nume % 2==0:
             print(f"el valor:{nume} es par y negativo")
             luigi=True
             par=par+1
             nega=nega+1
            elif nume<0 and nume % 2!=0:
                print(f"el valor:{nume} es inpar y negativo")
                luigi=True
                nega=nega+1
                inpar=inpar+1
        except ValueError:
            print("el comando ingresado no es un caracter numerico")
            print("porfavor ingrese un numero")
            luigi=False

print("--------------------------------")
print("----------------")
print(f"la cantidad de numeros pasitivos son:{positivos}")
print(f"la cantidad de numeros par son:{par}")
print(f"la cantidad de numeros negativos son:{nega}")
print(f"la cantidad de numeros inpar son:{inpar}")

#punto nueve:9)

print("calculando la media de un numero")
sumas=0
canti=0
for belgrano in range(5,0,-1):
    jojo=False
    while jojo==False:
        try:
         numer=int(input("ingrese un numero"))
         sumas=numer+sumas
         canti=canti+1
         print("-----------------------------")
         jojo=True
        except ValueError:             
         print("el caracter ingresado no es el solicitado")
         jojos=False
resu=sumas/canti
print(f"la media de todos los numeros dados es:{resu}")
    
 #punto diez:10)) 
patricio=False
while patricio==False:
 print("invirtiendo numeros")
 print("------------")
 print("ingrese un numero")
 num=str(input("__"))
 if num.isdigit():
       patricio=True
 else:
       patricio=False 

largo=len(num)
resu=""
if largo==1:
 print("el numero ingresado solo tiene un digito no es posible reordenarlos")
else: 
   for largo in range(largo,0,-1):
       nuev=num[-1]
       vie=num[:-1]
       resu=nuev + vie

print(resu)



























