from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

# Crear una tienda (puede ser de cualquier tipo, por ejemplo, Restaurante)
tienda = Restaurante("La buena mesa", 1000)
print(tienda)

while True:
    accion = input("Ingrese acción (agregar, listar, vender, salir): ")
    if accion == "salir":
        break
    elif accion == "agregar":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock (opcional, 0 por defecto): "))
        producto = Producto(nombre, precio, stock)
        tienda.ingresar_producto(producto)
    elif accion == "listar":
        print(tienda.listar_productos())
    elif accion == "vender":
        nombre_producto = input("Nombre del producto a vender: ")
        cantidad = int(input("Cantidad: "))
        tienda.realizar_venta(nombre_producto, cantidad)
