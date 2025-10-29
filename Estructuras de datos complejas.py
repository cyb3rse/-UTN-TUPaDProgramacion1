#punto 1) Dado el diccionario precios_frutas
precios_frutas={
    'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450

}
#Añadir las siguientes frutas con sus respectivos precios:
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)

#punto 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
precios_frutas={
    'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450

}

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)
print("-------------------------------------------")
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(precios_frutas)

# punto 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.
precios_frutas={
    'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450

}

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)
print("-------------------------------------------")
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(precios_frutas)
print("-------------------------------------------------")
print("solo las frutas disponibles")
only_frutas=precios_frutas.keys()
print(only_frutas)
print("-------------------------------------------------")

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
nombre_telefonos={}
nombre=""
numero=""
end_cen=False
while end_cen== False:
    salia_a_menu=False
    validacion=False
    print("-----------------------------------------")
    print("contactos/telefonos")
    print("que es lo que quiere hacer")
    print("para agregar un nombre apriete:__1")
    print("para agregar u numero apriete:__2 ")
    print("para mostrar los numero asociados a los elementos:__3")
    print("para salir:__4")
    eleccion=str(input(":_"))
    if eleccion.isdigit() and eleccion=="1":
        while salia_a_menu==False:
            nombre=str(input("ingrese el nombre que quiere agregar(limite de 5) "))
            nombre_telefonos[nombre]=None
            print("desea ingresar otro nombre?")
            print("para si ingrese:__1")
            print("para no ingrese:__2")
            confir=str(input(":__"))
              
            if confir.isdigit and confir=="1":
                salia_a_menu=False
            elif confir.isdigit and confir=="2":
                salia_a_menu=True
             
            if len(nombre_telefonos)>5:
                print("ya no se pueden agregar mas nombres regresando al menu....")
                salia_a_menu=True
             
    elif eleccion.isdigit() and eleccion=="2": 
        while salia_a_menu==False:
            while validacion==False:
                nombre=str(input("ingrese el nombre que quiere agregar el valor "))
                if nombre in nombre_telefonos:
                    while validacion==False:
                        print("que numero quiere asignarle?")
                        valor=str(input(":__"))
                        if valor.isdigit():
                            valor=int(valor)
                            nombre_telefonos[nombre]=valor
                            validacion=True
                        else:
                            print("a ingresado un valor no numerico intentelo devuelta:")
                            print("-----------------------------------------")
                         
                     
                else:
                    print("el nombre ingresado no se enccuentra")
                    print("-----------------------------------------")
            print("desea ingresar otro numero a un nombre?")
            print("para /si/ ingrese:__1")
            print("para /no/ ingrese:__2")
            confir=str(input(":__"))
             
            if confir.isdigit and confir=="1":
                salia_a_menu=False
                validacion=False
            elif confir.isdigit and confir=="2":
                salia_a_menu=True
             
    elif eleccion.isdigit() and eleccion=="3":
        print(f"los nombres con sus numeros actuales son:{nombre_telefonos}" )
    elif eleccion.isdigit() and eleccion=="4":
        end_cen=True
    else:
        print("porfavor ingrese unas de las opciones disponibles")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Escriba una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras unicas:", palabras_unicas)
contador={}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Cantidad de veces que aparece cada palabra:")
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")

# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno. 

estudiantes = []
for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        notas.append(nota)

    estudiante = (nombre, tuple(notas))
    estudiantes.append(estudiante)

print("Estudiantes y sus notas:")
for est in estudiantes:
    print(f"{est[0]}: {est[1]}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial1 = {"estudiante 1", "estudiante 2", "estudiante 3", "estudiante 4"}
parcial2 = {"estudiante 3", "estudiante 4", "estudiante 5", "estudiante 6"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los parciales:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

stock = {
    "Notebook": 5,
    "Celular": 8,
    "Auriculares": 15,
    "Silla": 3
}
print(" Stock inicial:", stock)
producto = input("\nIngrese el nombre del producto: ")

if producto in stock:
    print(f"El producto '{producto}' tiene {stock[producto]} unidades en stock.")
    decicion = input("¿Desea agregar unidades? (s/n): ").lower()
    if decicion == "s":
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        stock[producto] += cantidad
        print(f" Se agregaron {cantidad} unidades. Nuevo stock de {producto}: {stock[producto]}")
    else:
        print("No se realizaron cambios.")

else:
    print(f"El producto '{producto}' no existe en el stock.")
    agregar_nuevo = input("¿Desea agregarlo? (s/n): ").lower()
    if agregar_nuevo == "s":
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock[producto] = cantidad
        print(f" Producto '{producto}' agregado con {cantidad} unidades.")
    else:
        print("No se agregó el producto.")


print(" Stock actualizado:", stock)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.  
#Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ("lunes", "10:00"): "matematica",
    ("martes", "14:00"): "ingles",
    ("miércoles", "09:00"): "Gimnasia",
    ("viernes", "18:00"): "joda"
}

print("agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave[0]} a las {clave[1]} → {evento}")

dia = input("Ingrese un dia: ").lower()
hora = input("Ingrese una hora (formato HH:MM): ")
clave = (dia, hora)

if clave in agenda:
    print(f"el {dia} a las {hora} tenes: {agenda[clave]}")
else:
    print(f"no hay ninguna actividad registrada el {dia} a las {hora}.")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores.

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

print("paises y sus capitales:")
print(paises)

print("capitales como claves:")
print(capitales)