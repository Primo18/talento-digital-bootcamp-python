def solicitar_input(pregunta):
    respuesta = input(pregunta + " (si/no): ").strip().lower()
    while respuesta not in ["si", "no"]:
        respuesta = input("Por favor, responda con 'si' o 'no': ").strip().lower()
    return respuesta == "si"

def primeros_auxilios():
    print("Inicio del protocolo de emergencia.\n")
    
    if solicitar_input("¿Responde a estímulos?"):
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
    else:
        print("Abrir la vía aérea.")
        if solicitar_input("¿Respira?"):
            print("Permitir posición de suficiente ventilación.")
        else:
            print("Administrar 5 ventilaciones y llamar a una ambulancia.")
            if not solicitar_input("¿Signos de vida?"):
                print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
    
    while not solicitar_input("¿Llegó la ambulancia?"):
        print("Reevaluar a la espera de la ambulancia.")
    
    print("Proceso finalizado. La ambulancia se ha hecho cargo de la situación.")


primeros_auxilios()
