def calcular_imc(peso_kg, altura_cm):
    altura_m = altura_cm / 100  # Convertir altura a metros
    imc = peso_kg / (altura_m ** 2)
    return round(imc, 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"


# Pedir datos al usuario
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en cm: "))

# Cálculo del IMC
imc = calcular_imc(peso, altura)
clasificacion = clasificar_imc(imc)

# Mostrar resultados
print(f"Tu IMC es: {imc}\nClasificación: {clasificacion}")


