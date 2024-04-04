from te import Te

print("Ingrese el número correspondiente al sabor deseado:")
print("1: Té negro\n2: Té verde\n3: Agua de hierbas")
sabor = int(input("Sabor: "))

print("Ingrese el formato deseado (300 o 500 gramos):")
formato = int(input("Formato: "))

sabor_texto, tiempo, recomendacion = Te.obtener_info(sabor)
precio = Te.obtener_precio(formato)

print("\nDetalle del pedido:")
print(f"Sabor del té: {sabor_texto}")
print(f"Formato: {formato} gramos")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación de consumo: {recomendacion}")
