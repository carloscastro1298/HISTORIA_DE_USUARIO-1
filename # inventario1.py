# inventario.py

# Solicitar el nombre del producto al usuario
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio del producto y validar que sea un número decimal válido
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# Solicitar la cantidad del producto y validar que sea un número entero válido
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

# Calcular el costo total multiplicando el precio por la cantidad
costo_total = precio * cantidad

# Mostrar la información del producto y el costo total en un formato claro
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# Este programa solicita al usuario el nombre, precio y cantidad de un producto.
# Luego valida que el precio sea un número decimal y que la cantidad sea un número entero.
# Después calcula el costo total multiplicando el precio por la cantidad
# y finalmente muestra toda la información del producto en pantalla.