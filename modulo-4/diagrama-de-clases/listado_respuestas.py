from usuario import Usuario


class ListadoRespuestas:
    def __init__(self, usuario: "Usuario"):
        self.__usuario = usuario
        self.__lista_respuestas = []

    @property
    def usuario(self) -> "Usuario":
        return self.__usuario

    @property
    def lista_respuestas(self) -> list:
        return self.__lista_respuestas
