import requests


# Función para obtener todos los usuarios de la API
def obtener_todos_los_usuarios():
    usuarios = []  # Lista para guardar todos los usuarios
    pagina = 1  # Comenzar en la página 1

    while True:  # Continuar hasta que no haya más páginas
        respuesta = requests.get(f"https://reqres.in/api/users?page={pagina}")
        data = respuesta.json()
        usuarios_pagina = data.get("data", [])

        # Si no hay usuarios, terminar el bucle
        if not usuarios_pagina:
            break

        # Agregar los usuarios de esta página a la lista total
        usuarios.extend(usuarios_pagina)

        # Incrementar el número de página para la próxima iteración
        pagina += 1

    return usuarios


# Función para obtener el id de un usuario por su nombre
def get_user_id_by_name(name):
    response = requests.get("https://reqres.in/api/users")
    users_data = response.json()
    for user in users_data["data"]:
        if user["first_name"] == name or user["last_name"] == name:
            return user["id"]
    return None


print("Requerimiento 1:")
# Obtener y imprimir todos los usuarios
todos_los_usuarios = obtener_todos_los_usuarios()
print(todos_los_usuarios)


print("\nRequerimiento 2:")
# Requerimiento 2: Crear un usuario
user_data = {"name": "Ignacio", "job": "Profesor"}
response = requests.post("https://reqres.in/api/users", data=user_data)
print("Código de respuesta: ", response.status_code)  # Imprimir el código de respuesta
created_user = response.json()  # Guardar el diccionario de respuesta
print(created_user)  # Imprimir la respuesta en pantalla


print("\nRequerimiento 3:")
# Requerimiento 3: Actualizar el usuario 'morpheus' * Lo cambie a Charles porque no existe Morpheus
morpheus_id = get_user_id_by_name("Charles")  #
if morpheus_id:
    user_update = {"name": "Charles", "job": "leader", "residence": "zion"}
    response = requests.put(
        f"https://reqres.in/api/users/{morpheus_id}", data=user_update
    )
    updated_user = response.json()
    print("Código de respuesta: ", response.status_code)
    print(updated_user)
else:
    print("Usuario 'morpheus' no encontrado.")


print("\nRequerimiento 4:")
# Requerimiento 4: Eliminar el usuario 'Tracey'
tracey_id = get_user_id_by_name("Tracey")
if tracey_id:
    response = requests.delete(f"https://reqres.in/api/users/{tracey_id}")
    print(
        f"Código de respuesta para la eliminación de 'Tracey': {response.status_code}"
    )
else:
    print("Usuario 'Tracey' no encontrado.")
