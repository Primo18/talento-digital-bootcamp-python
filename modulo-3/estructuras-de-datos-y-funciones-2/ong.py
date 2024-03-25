def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def productoria(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


def calcular(**kwargs):
    for nombre, valor in kwargs.items():
        if "fact" in nombre:
            print(f"El factorial de {valor} es {factorial(valor)}")
        elif "prod" in nombre:
            print(f"La productoria de {valor} es {productoria(valor)}")


# Ejemplo de uso
calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)

# Salida esperada
# El factorial de 5 es 120
# La productoria de [4, 6, 7, 4, 3] es 2016
# El factorial de 6 es 720
