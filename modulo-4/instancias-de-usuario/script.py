import json
from usuario import Usuario


def main():
    usuarios = []  # Lista para almacenar las instancias de usuarios
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                try:
                    # Convertir la línea de texto en un diccionario
                    user_data = json.loads(line)
                    # Crear una instancia de Usuario con el diccionario desempaquetado
                    usuario = Usuario(**user_data)
                    usuarios.append(usuario)
                except Exception as e:
                    # En caso de una excepción, la registramos en el archivo error.log
                    with open("error.log", "a") as log_file:
                        log_file.write(f"Error al procesar la línea: {line}\n")
                        log_file.write(f"{str(e)}\n")
                        log_file.write("---------------------------------\n")
    except FileNotFoundError as e:
        print(f"El archivo no se encontró: {e}")
    except Exception as e:
        print(f"Un error ocurrió al leer el archivo: {e}")


if __name__ == "__main__":
    main()
