import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
opciones = {
    "basicas": ["pregunta_1", "pregunta_2", "pregunta_3"],
    "intermedias": ["pregunta_1", "pregunta_2", "pregunta_3"],
    "avanzadas": ["pregunta_1", "pregunta_2", "pregunta_3"],
}


def choose_q(dificultad):
    global opciones
    # Escoger preguntas por dificultad
    preguntas_disponibles = opciones[dificultad]
    # Escoger una pregunta aleatoriamente de las disponibles
    n_elegido = random.choice(preguntas_disponibles)
    # Eliminarla del listado global para no escogerla de nuevo
    preguntas_disponibles.remove(n_elegido)

    # Escoger enunciado y alternativas mezcladas
    pregunta = p.pool_preguntas[dificultad][n_elegido]
    enunciado = pregunta["enunciado"][
        0
    ]  # Asumiendo que el enunciado es una lista con un único elemento
    alternativas = shuffle_alt(pregunta)

    return enunciado, alternativas


if __name__ == "__main__":
    # Si ejecuto el programa, las preguntas cambian de orden, pero nunca deberían repetirse
    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")

    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")

    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")
