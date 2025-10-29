#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

productos = [
    "notebook,1200,5\n",
    "auriculares,100,10\n",
    "celular,800,8\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)  

print("archivo 'productos.txt' creado con éxito.")

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open("productos.txt", "r") as archivo:
  
 for linea in archivo:  
        linea = linea.strip()
        partes = linea.split(",")
        nombre = partes[0]
        precio = float(partes[1]) 
        cantidad = int(partes[2])     

        print(f"producto:{nombre}|precio:{precio}|cantidad:{cantidad}")

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt", "r") as archivo:
    print("productos existentes:")
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        nombre = partes[0]
        precio = float(partes[1])
        cantidad = int(partes[2])
        print(f"producto:{nombre}|precio:{precio}|cantidad:{cantidad}")

print("agregar un nuevo producto:")
nuevo_nombre = input("nombre:")
nuevo_precio = float(input("precio:"))
nueva_cantidad = int(input("cantidad:"))

with open("productos.txt","a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

print(f"producto {nuevo_nombre} agregado correctamente.")


#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()         
        partes = linea.split(",")    
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(producto)

for p in productos:
    print(p)

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

nombre_buscar = input("ingrese el nombre del producto que quiere buscar: ")
encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():  # ignorar mayúsculas/minúsculas
        print(f"producto encontrado:")
        print(f"nombre: {producto['nombre']}")
        print(f"precio: {producto['precio']}")
        print(f"cantidad: {producto['cantidad']}")
        encontrado = True
        break  

if not encontrado:
    print(f"a sucedido un error:el producto {nombre_buscar} no existe en la lista.")



#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(producto)

print("productos existentes:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

nombre_buscar = input("\nIngrese el nombre de un producto a buscar: ")
encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print(f"El producto '{nombre_buscar}' no existe.")

print("\nAgregar un nuevo producto:")
nuevo_nombre = input("Nombre: ")
nuevo_precio = float(input("precio: "))
nuevo_cantidad = int(input("cantidad: "))
nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nuevo_cantidad
}
productos.append(nuevo_producto)
print(f"producto '{nuevo_nombre}' agregado correctamente.")

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo 'productos.txt' actualizado correctamente.")





