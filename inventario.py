inventario ={}
def agregar_producto():
    codigo = input ("Ingrese el codigo de barras: ")
    nombre = input("Ingrese nombre del producto: ")
    cantidad= int(input("Ingrese cantidad: "))
    precio= float(input("Ingrese precio unitario:"))

    inventario[codigo] = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
        }
def ver_inventario():
    if not inventario:
        print("Inventario vacio")
    else:
        for codigo, datos in inventario.items():
            print("-------------------------")
            print("Codigo", codigo)
            print("Nombre:", datos["nombre"])
            print("Cantidad:", datos["precio"])
            print("Precio:", datos["precio"])