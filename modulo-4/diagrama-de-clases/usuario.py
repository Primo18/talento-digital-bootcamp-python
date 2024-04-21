class Usuario:
    def __init__(self, nombre: str, correo: str, edad: int, region: int):
        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    def contestar_encuesta(self, encuesta) -> None:

        print(f"Respondiendo a la encuesta: {encuesta.nombre}")

    # Métodos para obtener la información del usuario

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def correo(self) -> str:
        return self.__correo

    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def region(self) -> int:
        return self.__region

    # Métodos para establecer la información del usuario
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @correo.setter
    def correo(self, nuevo_correo: str) -> None:
        self.__correo = nuevo_correo

    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        self.__edad = nueva_edad

    @region.setter
    def region(self, nueva_region: int) -> None:
        self.__region = nueva_region
