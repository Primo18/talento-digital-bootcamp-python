import preguntas as p


def verificar(alternativas, eleccion):
    # Convertir la elección dada (letra) en su índice numérico correspondiente
    indice_eleccion = ["a", "b", "c", "d"].index(eleccion)

    # Determinar si la alternativa elegida es correcta
    correcto = alternativas[indice_eleccion][1] == 1

    # Imprimir el resultado de la verificación
    if correcto:
        print("Respuesta Correcta")
    else:
        print("Respuesta Incorrecta")

    return correcto


if __name__ == "__main__":
    from print_preguntas import print_pregunta

    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas["basicas"]["pregunta_2"]
    print_pregunta(pregunta["enunciado"], pregunta["alternativas"])
    respuesta = input("Escoja la alternativa correcta (a, b, c, d):\n> ").lower()
    verificar(pregunta["alternativas"], respuesta)
