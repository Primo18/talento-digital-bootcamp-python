from .models import Vehiculo, Chofer, RegistroContabilidad
from django.shortcuts import get_object_or_404


# Servicio para crear un vehículo
def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo.objects.create(
        patente=patente, marca=marca, modelo=modelo, year=year
    )
    return vehiculo


# Servicio para crear un chofer
def crear_chofer(rut, nombre, apellido):
    chofer = Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido)
    return chofer


# Servicio para crear un registro contable
def crear_registro_contable(vehiculo_patente, fecha_compra, valor):
    vehiculo = get_object_or_404(Vehiculo, patente=vehiculo_patente)
    registro = RegistroContabilidad.objects.create(
        vehiculo=vehiculo, fecha_compra=fecha_compra, valor=valor
    )
    return registro


# Servicio para deshabilitar un chofer
def deshabilitar_chofer(rut):
    chofer = get_object_or_404(Chofer, rut=rut)
    chofer.activo = False
    chofer.save()
    return chofer


# Servicio para deshabilitar un vehículo
def deshabilitar_vehiculo(patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    # Aquí puedes agregar lógica adicional si es necesario, como asegurar que el vehículo no esté en uso
    vehiculo.delete()
    return vehiculo


# Servicio para habilitar un chofer
def habilitar_chofer(rut):
    chofer = get_object_or_404(Chofer, rut=rut)
    chofer.activo = True
    chofer.save()
    return chofer


# Servicio para habilitar un vehículo
def habilitar_vehiculo(patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    # Aquí puedes agregar lógica adicional si es necesario
    # vehiculo.activo = True  # Si tienes un campo "activo", puedes descomentar esto
    vehiculo.save()
    return vehiculo


# Servicio para obtener la información de un vehículo
def obtener_vehiculo(patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    return vehiculo


# Servicio para obtener la información de un chofer
def obtener_chofer(rut):
    chofer = get_object_or_404(Chofer, rut=rut)
    return chofer


# Servicio para asignar un chofer a un vehículo
def asignar_chofer_a_vehiculo(rut, patente):
    chofer = get_object_or_404(Chofer, rut=rut)
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    chofer.vehiculo = vehiculo
    chofer.save()
    return chofer


# Servicio para imprimir los datos de todos los vehículos
def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    datos = []
    for vehiculo in vehiculos:
        datos.append(
            {
                "patente": vehiculo.patente,
                "marca": vehiculo.marca,
                "modelo": vehiculo.modelo,
                "year": vehiculo.year,
            }
        )
    return datos
