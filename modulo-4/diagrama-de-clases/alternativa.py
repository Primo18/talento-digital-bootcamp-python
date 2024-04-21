class Alternativa:
    def __init__(self, contenido: str, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        if self.ayuda:
            return f"{self.contenido} (Ayuda: {self.ayuda})"
        else:
            return self.contenido
