import random
from personaje import Personaje


def jugar():
    print("¡Bienvenido a Gran Fantasía!\n")
    nombre = input("Por favor indique nombre de su personaje: ")

    jugador = Personaje(nombre)
    orco = Personaje("Orco")

    jugador.obtener_estado()
    probabilidad = jugador.probabilidad_vs(orco)

    while True:
        opcion = Personaje.mostrar_dialogo(probabilidad)

        if opcion == 1:
            resultado = random.uniform(0, 1) <= probabilidad / 100
            if resultado:
                print("¡Le has ganado al orco, felicidades!")
                jugador.asignar_estado(50)
                orco.asignar_estado(-30)
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                jugador.asignar_estado(-30)
                orco.asignar_estado(50)

            jugador.obtener_estado()
            orco.obtener_estado()
            probabilidad = jugador.probabilidad_vs(orco)
        else:
            print("¡Has huido! El orco ha quedado atrás.")
            break


if __name__ == "__main__":
    jugar()
