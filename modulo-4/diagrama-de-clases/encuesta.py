from listado_respuestas import ListadoRespuestas
from pregunta import Pregunta
from usuario import Usuario


class Encuesta:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__preguntas = []
        self.__listado_respuestas = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        self.__nombre = valor

    def agregar_pregunta(self, pregunta: Pregunta):
        self.__preguntas.append(pregunta)

    def agregar_respuestas(self, respuestas: ListadoRespuestas):
        self.__listado_respuestas.append(respuestas)

    def mostrar_encuesta(self):
        print(f"Encuesta: {self.__nombre}")
        for pregunta in self.__preguntas:
            pregunta.mostrar()


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int):
        super().__init__(nombre)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    @property
    def edad_minima(self) -> int:
        return self.__edad_minima

    @edad_minima.setter
    def edad_minima(self, valor: int):
        self.__edad_minima = valor

    @property
    def edad_maxima(self) -> int:
        return self.__edad_maxima

    @edad_maxima.setter
    def edad_maxima(self, valor: int):
        self.__edad_maxima = valor

    def validar_edad(self, usuario: Usuario) -> bool:
        return self.__edad_minima <= usuario.edad <= self.__edad_maxima

    def agregar_respuestas(self, respuestas: "ListadoRespuestas"):
        if self.validar_edad(respuestas.usuario):
            super().agregar_respuestas(respuestas)
        else:
            print("Usuario no cumple con el criterio de edad para esta encuesta.")


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, regiones_permitidas: list):
        super().__init__(nombre)
        self.lista_regiones = regiones_permitidas

    @property
    def regiones_permitidas(self) -> list:
        return self.lista_regiones

    @regiones_permitidas.setter
    def regiones_permitidas(self, valor: list):
        self.lista_regiones = valor

    def validar_region(self, usuario: Usuario) -> bool:
        return usuario.region in self.lista_regiones

    def agregar_respuestas(self, respuestas: "ListadoRespuestas"):
        if self.validar_region(respuestas.usuario):
            super().agregar_respuestas(respuestas)
        else:
            print("Usuario no cumple con el criterio de región para esta encuesta.")
