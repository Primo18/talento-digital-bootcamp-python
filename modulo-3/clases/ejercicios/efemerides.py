# definimos el diccionario
efemerides = {
    "1 de Enero": "Año Nuevo",
    "27 de Febrero": "Terremoto en Chile",
    "8 de Marzo": "Día de la Mujer",
    "21 de Mayo": "Glorias Navales",
    "18 de Septiembre": "Fiestas Patrias",
    "19 de Septiembre": "Glorias del Ejercito",
    "25 de Diciembre": "Navidad",
}

fecha = input("Ingrese una fecha (formato: dd de Mes): ").lower()
print(efemerides.get(fecha, "No hay información para esa fecha"))
