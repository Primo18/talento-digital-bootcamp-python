from error import DimensionError


class Foto:
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.__ruta = (
            ruta  # Aquí debemos utilizar self para asignar a la variable de instancia.
        )

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        if not 1 <= ancho <= Foto.MAX:
            raise DimensionError(
                f"El ancho proporcionado ({ancho}) es inválido.",
                dimension=ancho,
                maximo=Foto.MAX,
            )
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        if not 1 <= alto <= Foto.MAX:
            raise DimensionError(
                f"El alto proporcionado ({alto}) es inválido.",
                dimension=alto,
                maximo=Foto.MAX,
            )
        self.__alto = alto

    # Asumiendo que puede ser necesario un getter para la ruta también.
    @property
    def ruta(self) -> str:
        return self.__ruta
