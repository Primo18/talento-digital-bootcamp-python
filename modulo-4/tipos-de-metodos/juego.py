import random
from personaje import Personaje


def jugar():
    print("¡Bienvenido a Gran Fantasía!\n")
    nombre = input("Por favor indique nombre de su personaje: ")

    jugador = Personaje(nombre)
    orco = Personaje("Orco")

    print(jugador)  # Imprime usando __str__
    probabilidad = jugador.probabilidad_vs(orco)

    while True:
        opcion = Personaje.mostrar_dialogo(probabilidad)

        if opcion == 1:
            resultado = random.uniform(0, 1) <= probabilidad / 100
            if resultado:
                print("¡Le has ganado al orco, felicidades!")
                jugador.experiencia += 50  # Modifica directamente la experiencia
                orco.experiencia -= 30
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                jugador.experiencia -= 30
                orco.experiencia += 50

            print(jugador)  # Usa __str__ para imprimir el estado actualizado
            print(orco)
            probabilidad = jugador.probabilidad_vs(orco)
        else:
            print("¡Has huido! El orco ha quedado atrás.")
            break


if __name__ == "__main__":
    jugar()
