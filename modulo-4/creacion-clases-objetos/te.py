class Te:
    # Atributo de clase para la duración de todos los tés
    duracion = 365  # días

    @staticmethod
    def obtener_info(sabor):
        """Retorna el tiempo de preparación y recomendación según el sabor."""
        sabores = {
            1: ("Té negro", 3, "Desayuno"),
            2: ("Té verde", 5, "Medio día"),
            3: ("Agua de hierbas", 6, "Atardecer")
        }
        return sabores.get(sabor, ("Sabor no definido", 0, "No hay recomendación"))

    @staticmethod
    def obtener_precio(formato):
        """Retorna el precio según el formato."""
        precios = {
            300: 3000,
            500: 5000
        }
        return precios.get(formato, 0)
