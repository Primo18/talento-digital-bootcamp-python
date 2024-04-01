import http.client

# conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
# payload = ""
# headers = {}
# conn.request("GET", "/posts", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

mi_diccionario = {"a": 1, "b": 2, "c": 3}

for clave in mi_diccionario:
    print(clave)  # Imprime las claves del diccionario

for valor in mi_diccionario.values():
    print(valor)  # Imprime los valores del diccionario


prefijo = ["La", "El", "La", "El"]
frutas = ["manzana", "platano", "frutilla", "tomate"]
colores = ["verde", "amarillo", "roja", "rojo"]
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f"{p} {fruta} es de color {color}")


cuadrados_dict = {x: x**2 for x in range(10)}

print(cuadrados_dict)
