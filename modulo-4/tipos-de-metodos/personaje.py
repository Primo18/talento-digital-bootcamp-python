class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        print(f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}")

    def asignar_estado(self, exp):
        self.experiencia += exp
        while self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
        while self.experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            self.experiencia += 100
        if self.nivel == 1 and self.experiencia < 0:
            self.experiencia = 0

    def __gt__(self, otro):
        return self.nivel > otro.nivel

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
