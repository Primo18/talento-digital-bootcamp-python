import logging
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction
from .models import Conductor, Direccion, Vehiculo

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constantes
RUT_LENGTH = 9
ERROR_RUT_INVALID = "El RUT debe tener 9 dígitos y ser válido"
ERROR_CONDUCTOR_EXISTS = "El conductor ya existe"
ERROR_CONDUCTOR_NOT_FOUND = "El conductor no existe"
ERROR_DIRECCION_EXISTS = "La dirección ya existe"
ERROR_DIRECCION_NOT_FOUND = "La dirección no existe"
ERROR_VEHICULO_EXISTS = "El vehículo ya existe"
ERROR_VEHICULO_NOT_FOUND = "El vehículo no existe"


def log_modelo(modelo):
    logger.info(f"{modelo.__name__}s:")
    for obj in modelo.objects.all():
        logger.info(str(obj))
    logger.info("")


def imprimir_modelos():
    log_modelo(Conductor)
    log_modelo(Direccion)
    log_modelo(Vehiculo)


def validar_rut(rut):
    if len(rut) != RUT_LENGTH or not rut[:-1].isdigit() or rut[-1] not in "0123456789K":
        raise ValidationError(ERROR_RUT_INVALID)
    # Aquí puedes agregar más validaciones específicas del RUT chileno si lo deseas


def manejo_excepciones(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            logger.error(str(e))
            raise
        except Exception as e:
            logger.error(f"Error inesperado: {str(e)}")
            raise

    return wrapper


class ConductorManager:
    @staticmethod
    @manejo_excepciones
    @transaction.atomic
    def crear(rut, nombre, apellido, fecha_nacimiento):
        validar_rut(rut)
        if Conductor.objects.filter(rut=rut).exists():
            raise ValidationError(ERROR_CONDUCTOR_EXISTS)
        conductor = Conductor.objects.create(
            rut=rut, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento
        )
        imprimir_modelos()
        return conductor

    @staticmethod
    @manejo_excepciones
    def obtener(rut):
        try:
            return Conductor.objects.get(rut=rut)
        except ObjectDoesNotExist:
            raise ValidationError(ERROR_CONDUCTOR_NOT_FOUND)

    @staticmethod
    @manejo_excepciones
    @transaction.atomic
    def eliminar(rut):
        conductor = ConductorManager.obtener(rut)
        conductor.delete()
        imprimir_modelos()


class DireccionManager:
    @staticmethod
    @manejo_excepciones
    @transaction.atomic
    def crear(rut, calle, numero, comuna, ciudad, region):
        conductor = ConductorManager.obtener(rut)
        if Direccion.objects.filter(conductor=conductor).exists():
            raise ValidationError(ERROR_DIRECCION_EXISTS)
        direccion = Direccion.objects.create(
            conductor=conductor,
            calle=calle,
            numero=numero,
            comuna=comuna,
            ciudad=ciudad,
            region=region,
        )
        imprimir_modelos()
        return direccion

    @staticmethod
    @manejo_excepciones
    @transaction.atomic
    def eliminar(rut):
        conductor = ConductorManager.obtener(rut)
        direccion = Direccion.objects.filter(conductor=conductor).first()
        if not direccion:
            raise ValidationError(ERROR_DIRECCION_NOT_FOUND)
        direccion.delete()
        imprimir_modelos()


class VehiculoManager:
    @staticmethod
    @manejo_excepciones
    @transaction.atomic
    def agregar(patente, marca, modelo, ano, rut):
        conductor = ConductorManager.obtener(rut)
        if Vehiculo.objects.filter(patente=patente).exists():
            raise ValidationError(ERROR_VEHICULO_EXISTS)
        vehiculo = Vehiculo.objects.create(
            patente=patente, marca=marca, modelo=modelo, ano=ano, conductor=conductor
        )
        imprimir_modelos()
        return vehiculo

    @staticmethod
    @manejo_excepciones
    @transaction.atomic
    def eliminar(patente):
        vehiculo = Vehiculo.objects.filter(patente=patente).first()
        if not vehiculo:
            raise ValidationError(ERROR_VEHICULO_NOT_FOUND)
        vehiculo.delete()
        imprimir_modelos()
