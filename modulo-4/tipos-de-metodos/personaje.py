class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self._experiencia = 0

    # Getter para la experiencia
    @property
    def experiencia(self):
        return self._experiencia

    # Setter para la experiencia
    @experiencia.setter
    def experiencia(self, exp):
        self._experiencia += exp
        while self._experiencia >= 100:
            self.nivel += 1
            self._experiencia -= 100
        while self._experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            self._experiencia += 100
        if self.nivel == 1 and self._experiencia < 0:
            self._experiencia = 0

    # Método especial para imprimir el objeto
    def __str__(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self._experiencia}"

    # Método especial para comparar si un personaje es mayor que otro
    def __gt__(self, otro):
        return self.nivel > otro.nivel

    # Método especial para comparar si un personaje es menor que otro
    def __lt__(self, otro):
        return self.nivel < otro.nivel

    def probabilidad_vs(self, otro):
        if self > otro:
            return 66
        elif self < otro:
            return 33
        else:
            return 50

    @staticmethod
    def mostrar_dialogo(probabilidad):
        print(
            f"Con tu nivel actual, tienes {probabilidad}% de probabilidades de ganarle al Orco."
        )
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        return int(input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n"))
