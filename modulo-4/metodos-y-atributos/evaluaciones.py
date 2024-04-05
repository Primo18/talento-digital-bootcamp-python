from pizza import Pizza

# a. Mostrar los valores de los atributos de clase sin crear una instancia
print(Pizza.ingredientes_proteicos)
print(Pizza.ingredientes_vegetales)
print(Pizza.tipos_de_masa)

# b. Validar un elemento sin crear una instancia
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Crear una instancia y llamar al método para realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar los ingredientes y el tipo de masa de la instancia creada, y si es válida
print(
    f"Proteico: {mi_pizza.ingrediente_proteico}, Vegetales: {mi_pizza.ingrediente_vegetal1}, {mi_pizza.ingrediente_vegetal2}, Masa: {mi_pizza.tipo_de_masa}, Válida: {mi_pizza.es_valida}"
)

# e. Intentar mostrar si Pizza es una pizza válida sin crear una instancia (debería dar error ya que es un atributo de instancia y no de clase)
print(Pizza.es_valida)  # Esta línea causará un AttributeError al ejecutar
