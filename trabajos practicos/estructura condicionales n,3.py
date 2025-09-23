#PUNTO UNO

edad=(input("ingrese, para confirmar su edad:"))
 
if Edad<18:
  print("usted es menor de edad no puede ingresar")
else:
 print("Es mayor de edad")

#PUNTO DOS
nota=int(input("ingrese su nota para calificarla:"))
if nota>=6 and nota<=10:
    print("usted esta aprobado")
elif nota<6 and nota>=0:
    print("usted esta desaprobado intente mejor la proxima")
else:
    print("la nota ingresada no corresponde a este sistema de medicion")

#PUNTO TRES


num=int(input("ingrese un numero para saber si es par o no:"))
if num % 2==0:
    print(" a ingresado un numero par")
else:
    print("el numero ingresado es impar")

#PUNTO CUATRO


edad=int(input("ingrese su edad para evaluarlo:"))
if edad<12 and edad >=0:
    print("usted es un niño/a")
elif edad>=12 and edad<18:
    print("usted es un adolecente")
elif edad>=18 and edad<30:
    print("usted es un adulto/a joven")
elif edad>=30 and edad<=100:
    print("usted es adulto/a")
elif edad>100:
    print("usted es adulto/a (fosil)")
else:
   pass

#PUNTO CINCO

contra=str(input("ingrese una contraseña de entre 8 y 14 caracteres:"))
cantida=len(contra)
if  cantida>=8 and cantida<=14:
    print("ha ingresado una contraseña correcta")
else:
    print(f"usted solo a colocado una contraseña de {cantida} caracteres")
    print("por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#PUNTO SEIS
import statistics
import random
print("vamos a tomar la median, el mode y mean de numeros aleatorios")
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
nume = statistics.median(numeros_aleatorios)
numo=statistics.mode(numeros_aleatorios)
numean=statistics.mean(numeros_aleatorios)
print(f"la moda de esos numero aleatorios es:{numo}")
print(f"la mediana de esos numero aleatorios es:{nume}")
print(f"y la media de esos numero aleatorios es:{numean}")
print("entonces el sesgo que hay es : ")
if numean> nume and nume>numo:
 print("POSITIVO")
elif numean<nume and nume<numo:
   print("NEGATIVO")
elif numean==nume and nume ==numo:
   print("NINGUNO")
else:
   print("no hay ningun sesgo aplicable posible")

#PUNTO SIETE
frase=input("ingrese una letra o una frase:")
vocal=('A','E','I','O','U')
VACALAO=('a','e','i','o','u')
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
if frase[-1] in vocal or frase[-1] in VACALAO:
   frase=frase+"!!!!!!!!!!!!"
   print("aqui esta su frase/letra:")
   print(frase)
else: 
   print("aqui esta su frase/letra:")
   print(frase)
#PUNTO OCHO
nom=str(input("ingrese su nombre:"))
print("ahora seleccione una opcion segun como quiera modificarlo:")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")                                                            
print("3. Si quiere su nombre con la primera letra mayúscula")
print("4. si quiere su nombre sin ninguna modificacion")
num=float(input("-------->:"))
if num==1:
  rea=str.upper(nom) 
  print(rea)
elif num==2:
 rea=str.lower(nom)
 print(rea)
elif num==3:
 rea = str.title(nom)
 print(rea)
elif num==4:
 print(nom)
else:
    print("la opcion selecciona no se encuentra entre las disponibles.")
#PUTO NUEVE
mag=float(input("ingrese la magnitud del terremoto actual para clasificar su escala de peligro:"))
if mag<3.00:
   print("Menor que 3:_Muy_leve_(imperceptible).")
   print("no se encuentra en peligro, puede estar seguro")
elif mag>=3.00 and mag<4.00:
   print("Mayor o igual que 3 y menor que 4:_Leve_(ligeramente perceptible).")
   print("cuidado con no caerse")
elif mag>=4.00 and mag<5.00:
   print("Mayor o igual que 4 y menor que 5:_Moderado_(sentido por personas, pero generalmente no causa daños)")
elif mag>=5.00 and mag<6.00:
   print("Mayor o igual que 5 y menor que 6:_Fuerte_(puede causar daños en estructuras débiles).")
elif mag>=6.00 and mag<7.00:
    print("mayor o igual que 6 y menor que 7:_Muy_Fuerte_(puede causar daños significativos).")
elif mag>=7.00:
   print("Mayor o igual que 7:_Extremo_(puede causar graves daños a gran escala).")


#PUNTO 10
print("ingrese los datos correspondientes para analizar en que estacion esta:")
hemi=input("ingrese en que emisferio se encuentra con la inicial del emisferios   Norte/Sur:")
dia=float(input("ingrese el dia del año se encuenta actualmente:"))
mes=float(input("ingrese numero del mes del que se encuenta actualmente:"))
if dia<=31  and dia >0 and mes<=12 and mes >=1 and hemi in "nNsS" or hemi:
   dia= dia/100
   diames=mes+ dia
   
   if diames>=12.21 and diames<=12.31 or diames >=1.01 and diames<=3.20:
      if hemi in"nN":
         print("usted actualmente se encuentra en invierno")    
      else:
         print("usted actualmente se encuentra en verano")
   elif diames>=3.21 and diames <=6.20:
       if  hemi in"nN":
         print("usted actuamlmente se encuentra en primavera")
       else:
         print("usted actuamlmente se encuentra en otoño") 
   elif diames>=6.21 and diames <=9.20:
       if  hemi in "nN":
         print("usted actualmente se encuentra en verano")
       else:
         print("usted actualmente se encuentra en invierno")
   elif diames>=9.21 and diames <=12.20:
       if  hemi in "nN": 
         print("usted actuamlmente se encuentra en otoño")
       else:
         print("usted actuamlmente se encuentra en primavera")
else:
  print("los  datos ingresados no son los datos pedidos")





















































