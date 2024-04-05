class Pizza:
    # Atributos de clase según el problema
    ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_de_masa = ["tradicional", "delgada"]

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_de_masa = None
        self.es_valida = False  # Atributo para saber si la pizza es válida

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def realizar_pedido(self):
        self.ingrediente_proteico = input("Ingresa el ingrediente proteico: ")
        self.ingrediente_vegetal1 = input("Ingresa el primer ingrediente vegetal: ")
        self.ingrediente_vegetal2 = input("Ingresa el segundo ingrediente vegetal: ")
        self.tipo_de_masa = input("Ingresa el tipo de masa: ")

        # Validar los ingredientes y el tipo de masa
        if (
            self.validar_elemento(
                self.ingrediente_proteico, self.ingredientes_proteicos
            )
            and self.validar_elemento(
                self.ingrediente_vegetal1, self.ingredientes_vegetales
            )
            and self.validar_elemento(
                self.ingrediente_vegetal2, self.ingredientes_vegetales
            )
            and self.validar_elemento(self.tipo_de_masa, self.tipos_de_masa)
        ):
            self.es_valida = True
