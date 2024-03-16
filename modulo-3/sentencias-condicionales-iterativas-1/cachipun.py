import sys
import random

# Función para jugar Cachipún contra el computador
def jugar_cachipun(eleccion_usuario):
    opciones = ['piedra', 'papel', 'tijera']
    eleccion_computador = random.choice(opciones)
    
    if eleccion_usuario not in opciones:
        return f"Argumento inválido: Debe ser piedra, papel o tijera. Tus opciones eran: {', '.join(opciones)}"
    
    # Determinar el ganador
    if eleccion_usuario == eleccion_computador:
        resultado = "Empate!"
    elif (eleccion_usuario == "piedra" and eleccion_computador == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_computador == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_computador == "papel"):
        resultado = "Ganaste!!"
    else:
        resultado = "Perdiste :("
    
    return f"Tu jugaste {eleccion_usuario.capitalize()}\nComputador jugó {eleccion_computador}\n{resultado}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: cachipun.py <piedra|papel|tijera>")
        sys.exit(1)
    
    eleccion_usuario = sys.argv[1]
    resultado = jugar_cachipun(eleccion_usuario)
    print(resultado)

    



