from error import SubTipoInvalidoError


class Anuncio:
    # Las subclases definirán SUB_TIPOS y FORMATO
    SUB_TIPOS = None
    FORMATO = None

    def __init__(
        self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str
    ):
        self._ancho = max(1, ancho)
        self._alto = max(1, alto)
        self._url_archivo = url_archivo
        self._url_clic = url_clic
        self.sub_tipo = sub_tipo  # Validación realizada en el setter

    @property
    def ancho(self) -> int:
        return self._ancho

    @property
    def alto(self) -> int:
        return self._alto

    @property
    def url_archivo(self) -> str:
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, valor: str) -> None:
        self._url_archivo = valor

    @property
    def url_clic(self) -> str:
        return self._url_clic

    @url_clic.setter
    def url_clic(self, valor: str) -> None:
        self._url_clic = valor

    @property
    def sub_tipo(self) -> str:
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor: str) -> None:
        if self.SUB_TIPOS is not None and valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(
                f"El subtipo {valor} no es válido para el formato {self.FORMATO}."
            )
        self._sub_tipo = valor

    @classmethod
    def mostrar_formatos(cls):
        print(f"FORMATO {cls.FORMATO}:")
        print("==========")
        for subtipo in cls.SUB_TIPOS:
            print(f"- {subtipo}")

    def comprimir_anuncio(self):
        raise NotImplementedError

    def redimensionar_anuncio(self):
        raise NotImplementedError


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, duracion: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._duracion = max(5, duracion)
        self._ancho = 1  # Ancho fijo según especificación
        self._alto = 1  # Alto fijo según especificación

    @property
    def duracion(self) -> int:
        return self._duracion

    @duracion.setter
    def duracion(self, valor: int) -> None:
        self._duracion = max(5, valor)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
