class Pregunta:
    def __init__(self, enunciado: str, requerido: bool, ayuda: str = None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.esRequerida = requerido
        self.alternativas = []

    def mostrar_pregunta(self):
        resultado = f"Pregunta: {self.enunciado}"
        if self.ayuda:
            resultado += f" (Ayuda: {self.ayuda})"
        resultado += "\nAlternativas:"
        for alt in self.alternativas:
            resultado += f"\n - {alt.mostrar()}"
        return resultado
