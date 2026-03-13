# 📦 Inventario en Python
Este proyecto consiste en un script sencillo en Python que permite registrar un producto y calcular su costo total dentro de un inventario básico. 
El programa solicita información al usuario desde la consola, valida los datos ingresados y finalmente muestra un resumen del producto.

## ¿Como Funciona?
El programa realiza las siguientes acciones:
Solicita el nombre del producto
El usuario debe ingresar un nombre que contenga solo letras.
Si se ingresan números o símbolos, el programa muestra un mensaje de error y vuelve a solicitar el dato.
Solicita el precio del producto
El precio debe ser un número decimal válido.
Se utiliza manejo de errores (try / except) para evitar que el programa falle si el usuario ingresa texto u otro valor incorrecto.
Solicita la cantidad del producto
La cantidad debe ser un número entero.
Si el usuario ingresa un valor inválido, el sistema vuelve a pedir el dato.
Calcula el costo total
El costo total se obtiene multiplicando:
precio × cantidad
Muestra el resultado
Finalmente se imprime en pantalla un resumen con:
Nombre del producto
Precio
Cantidad
Total calculado

## 💻 Ejemplo de ejecución
Ingrese el nombre del producto: Lapiz
Ingrese el precio del producto: 1000
Ingrese la cantidad del producto: 4

Producto: Lapiz | Precio: 1000 | Cantidad: 4 | Total: 4000

![alt text](<HISTORIA DE USUARIO-2.jpg>)