from error import LargoExcedidoError
from datetime import datetime
from anuncio import Video, Display, Social


class Campaña:
    def __init__(
        self,
        nombre: str,
        fecha_inicio: datetime,
        fecha_termino: datetime,
        anuncios: list,
    ):
        if len(nombre) > 250:
            raise LargoExcedidoError(
                "El nombre de la campaña excede el largo permitido."
            )
        self._nombre = nombre
        self._anuncios = anuncios  # Debería ser una lista de instancias de Anuncio
        self._fecha_inicio = fecha_inicio
        self._fecha_termino = fecha_termino

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if len(valor) > 250:
            raise LargoExcedidoError(
                "El nombre de la campaña excede el largo permitido."
            )
        self._nombre = valor

    # Getters y setters para las fechas
    @property
    def fecha_inicio(self) -> datetime:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor: datetime) -> None:
        # Aquí podrías agregar lógica de validación si es necesario
        self._fecha_inicio = valor

    @property
    def fecha_termino(self) -> datetime:
        return self._fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor: datetime) -> None:
        # Aquí podrías agregar lógica de validación si es necesario
        self._fecha_termino = valor

    @property
    def anuncios(self) -> list:
        return self._anuncios

    def __str__(self) -> str:
        contador_anuncios = {"Video": 0, "Display": 0, "Social": 0}
        fecha_inicio_str = self._fecha_inicio.strftime("%Y-%m-%d")
        fecha_termino_str = self._fecha_termino.strftime("%Y-%m-%d")
        for anuncio in self._anuncios:
            if isinstance(anuncio, Video):
                contador_anuncios["Video"] += 1
            elif isinstance(anuncio, Display):
                contador_anuncios["Display"] += 1
            elif isinstance(anuncio, Social):
                contador_anuncios["Social"] += 1
        return (
            f"Nombre de la campaña: {self._nombre}\n"
            f"Fechas: Desde {fecha_inicio_str} hasta {fecha_termino_str}\n"
            f"Anuncios: {contador_anuncios['Video']} Video, "
            f"{contador_anuncios['Display']} Display, "
            f"{contador_anuncios['Social']} Social"
        )
