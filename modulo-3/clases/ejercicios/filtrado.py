a = [100, 200, 1000, 5000, 10000, 10, 5000]


filtered_list = [x for x in a if x <= 1000]
print(filtered_list)


b = [120, 50, 600, 30, 90, 10, 200, 0, 500]


# Se debe retornar una lista que clasifique todos los tiempos menores a 90 minutos
# como 'bien' y todos los tiempos mayores o iguales a 90 como 'mal'
filtered_list_b = ["bien" if x < 90 else "mal" for x in b]
print(filtered_list_b)


seconds = [100, 50, 1000, 5000, 1000, 500]

minutes = [x // 60 for x in seconds]
print(minutes)


diccionario = {
    "celular": 140000,
    "notebook": 489990,
    "tablet": 120000,
    "cargador": 12400,
}
del diccionario["celular"]
print(diccionario)
