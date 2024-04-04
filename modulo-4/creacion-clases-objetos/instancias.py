from te import Te

te1 = Te()
te2 = Te()

tipo_te1 = type(te1)
tipo_te2 = type(te2)

print(tipo_te1)
print(tipo_te2)

if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo.")
else:
    print("Los objetos no son del mismo tipo.")
