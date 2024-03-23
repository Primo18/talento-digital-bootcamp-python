def contar_elementos_distintos(texto):
    # Eliminar espacios y saltos de línea para el conteo de caracteres
    caracteres = texto.replace(" ", "").replace("\n", "")
    caracteres_distintos = len(set(caracteres))

    # Convertir a minúsculas antes de dividir
    texto_min = texto.lower()

    # Contar palabras distintas
    palabras_distintas = len(set(texto_min.split()))

    return caracteres_distintos, palabras_distintas


def main():
    import sys

    if len(sys.argv) != 2:
        print("Uso: python word_count.py <nombre_del_archivo>")
        sys.exit(1)

    nombre_del_archivo = sys.argv[1]

    try:
        # Abrir el archivo y leer su contenido
        with open(nombre_del_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

        # Contar caracteres y palabras distintas
        caracteres_distintos, palabras_distintas = contar_elementos_distintos(texto)

        # Imprimir los resultados
        print(f"El número de caracteres distintos es: {caracteres_distintos}")
        print(f"El número de palabras distintas es: {palabras_distintas}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_del_archivo}' no se encontró.")


if __name__ == "__main__":
    main()


# python word_count.py lorem_ipsum.txt
