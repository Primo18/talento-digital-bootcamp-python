from string import ascii_lowercase

def fuerza_bruta(password):
    intentos = 0
    for i in range(len(password)):
        for letra in ascii_lowercase:
            intentos += 1
            if letra == password[i]:
                break
    return intentos

# Ejemplo de uso
password = input("Ingrese la contraseña (la entrada no será ocultada): ")
intentos = fuerza_bruta(password)
print(f"La contraseña fue forzada en {intentos} intentos.")
