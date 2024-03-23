# Lista inicial de recordatorios
recordatorios = [
    ["2021-01-01", "11:00", "Levantarse y ejercitar"],
    ["2021-05-01", "15:00", "No trabajar"],  # Este evento será eliminado
    ["2021-07-15", "13:00", "No hacer nada es feriado"],  # Este evento será editado
    ["2021-09-18", "16:00", "Ramadas"],
    ["2021-12-25", "00:00", "Navidad"],
]

# 1. Agregar un evento el 2 de Febrero de 2021 a las 6 de la mañana para "Empezar el Año"
recordatorios.append(["2021-02-02", "06:00", "Empezar el año"])

# 2. Editar el evento del 15 de Julio para que sea el 16 de Julio
for evento in recordatorios:
    if evento[0] == "2021-07-15":
        evento[0] = "2021-07-16"

# 3. Eliminar el evento del día del trabajo (1 de Mayo)
recordatorios = [evento for evento in recordatorios if evento[0] != "2021-05-01"]

# 4. Agregar una cena de Navidad el 24 de Diciembre y de Año Nuevo el 31 de Diciembre, ambas a las 22:00 hrs
recordatorios.append(["2021-12-24", "22:00", "Cena de Navidad"])
recordatorios.append(["2021-12-31", "22:00", "Cena de Año Nuevo"])

# Ordenar la lista para asegurar el orden cronológico después de todas las ediciones
recordatorios.sort()

# Imprimir la lista final de recordatorios
print(recordatorios)
