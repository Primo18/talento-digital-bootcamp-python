from datetime import datetime, timedelta
from campaña import Campaña
from anuncio import Video
from error import SubTipoInvalidoError, LargoExcedidoError

# Crear las fechas de inicio y término para la campaña
fecha_inicio = datetime.now()
fecha_termino = datetime.now() + timedelta(days=30)  # Usa timedelta aquí correctamente

# Crear una instancia de Campaña con un anuncio de tipo Video
try:
    campaña = Campaña(
        nombre="Campaña de Lanzamiento",
        fecha_inicio=fecha_inicio,
        fecha_termino=fecha_termino,
        anuncios=[
            Video(
                duracion=30,
                ancho=1,
                alto=1,
                url_archivo="ruta/video.mp4",
                url_clic="http://clic_aqui.com",
                sub_tipo="instream",
            )
        ],
    )

    # Solicitar nuevo nombre de la campaña
    nuevo_nombre = input("Ingrese el nuevo nombre para la campaña: ")
    try:
        campaña.nombre = nuevo_nombre
    except LargoExcedidoError as e:
        with open("error.log", "a") as log_file:
            log_file.write(f"Error al cambiar el nombre de la campaña: {e}\n")

    # Solicitar nuevo subtipo para el anuncio
    nuevo_sub_tipo = input(
        "Ingrese el nuevo subtipo para el anuncio (instream/outstream): "
    )
    try:
        for anuncio in campaña.anuncios:
            anuncio.sub_tipo = nuevo_sub_tipo  # Suponiendo que todos los anuncios deben tener el mismo subtipo
    except SubTipoInvalidoError as e:
        with open("error.log", "a") as log_file:
            log_file.write(f"Error al cambiar el subtipo del anuncio: {e}\n")

    print(campaña)

except Exception as e:
    with open("error.log", "a") as log_file:
        log_file.write(f"Error inesperado: {e}\n")
