import sys

def convertir_monedas(tasas, monto_chileno):
    conversiones = [monto_chileno * tasa for tasa in tasas]
    return conversiones

if __name__ == "__main__":
    tasas = list(map(float, sys.argv[1:4]))
    monto_chileno = float(sys.argv[4])
    resultados = convertir_monedas(tasas, monto_chileno)
    monedas = ['Soles', 'Pesos Argentinos', 'Dólares']
    print(f"Los {monto_chileno} pesos equivalen a:")
    for moneda, resultado in zip(monedas, resultados):
        print(f"{resultado} {moneda}")


# Entrada:
# python conversiones.py 0.0046 0.093 0.0013 10000
        
# Salida:
#        46.0 Soles
#        930.0 Pesos Argentinos
#        13.0 Dólares