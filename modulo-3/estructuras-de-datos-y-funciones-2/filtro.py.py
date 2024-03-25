import sys

precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000,
}


def filtrar_productos(umbral, condicion="mayor"):
    filtrados = {}
    for producto, precio in precios.items():
        if condicion == "mayor" and precio > umbral:
            filtrados[producto] = precio
        elif condicion == "menor" and precio < umbral:
            filtrados[producto] = precio
    return filtrados


if __name__ == "__main__":
    umbral = float(sys.argv[1])
    condicion = sys.argv[2] if len(sys.argv) == 3 else "mayor"

    if condicion not in ["mayor", "menor"]:
        print("Lo sentimos, la condición ingresada no es válida.")
        sys.exit(1)

    productos_filtrados = filtrar_productos(umbral, condicion)

    print(
        f"Productos con precio {'mayor' if condicion == 'mayor' else 'menor'} a {umbral}:"
    )
    for producto, precio in productos_filtrados.items():
        print(f"{producto}: {precio}")
