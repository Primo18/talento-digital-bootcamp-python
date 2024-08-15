from django.http import JsonResponse, HttpResponseBadRequest
from .services import (
    crear_vehiculo,
    crear_chofer,
    crear_registro_contable,
    deshabilitar_chofer,
    deshabilitar_vehiculo,
    habilitar_chofer,
    habilitar_vehiculo,
    obtener_vehiculo,
    obtener_chofer,
    asignar_chofer_a_vehiculo,
    imprimir_datos_vehiculos,
)


# Vista para crear un vehículo
def crear_vehiculo_view(request):
    if request.method == "POST":
        patente = request.POST.get("patente")
        marca = request.POST.get("marca")
        modelo = request.POST.get("modelo")
        year = request.POST.get("year")
        if patente and marca and modelo and year:
            vehiculo = crear_vehiculo(patente, marca, modelo, year)
            return JsonResponse({"vehiculo": str(vehiculo)})
        else:
            return HttpResponseBadRequest("Faltan datos para crear el vehículo.")
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para crear un chofer
def crear_chofer_view(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        if rut and nombre and apellido:
            chofer = crear_chofer(rut, nombre, apellido)
            return JsonResponse({"chofer": str(chofer)})
        else:
            return HttpResponseBadRequest("Faltan datos para crear el chofer.")
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para crear un registro contable
def crear_registro_contable_view(request):
    if request.method == "POST":
        vehiculo_patente = request.POST.get("vehiculo_patente")
        fecha_compra = request.POST.get("fecha_compra")
        valor = request.POST.get("valor")
        if vehiculo_patente and fecha_compra and valor:
            registro = crear_registro_contable(vehiculo_patente, fecha_compra, valor)
            return JsonResponse({"registro": str(registro)})
        else:
            return HttpResponseBadRequest(
                "Faltan datos para crear el registro contable."
            )
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para deshabilitar un chofer
def deshabilitar_chofer_view(request, rut):
    if request.method == "POST":
        chofer = deshabilitar_chofer(rut)
        return JsonResponse({"chofer": str(chofer), "estado": "deshabilitado"})
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para deshabilitar un vehículo
def deshabilitar_vehiculo_view(request, patente):
    if request.method == "POST":
        vehiculo = deshabilitar_vehiculo(patente)
        return JsonResponse({"vehiculo": str(vehiculo), "estado": "deshabilitado"})
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para habilitar un chofer
def habilitar_chofer_view(request, rut):
    if request.method == "POST":
        chofer = habilitar_chofer(rut)
        return JsonResponse({"chofer": str(chofer), "estado": "habilitado"})
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para habilitar un vehículo
def habilitar_vehiculo_view(request, patente):
    if request.method == "POST":
        vehiculo = habilitar_vehiculo(patente)
        return JsonResponse({"vehiculo": str(vehiculo), "estado": "habilitado"})
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para obtener la información de un vehículo
def obtener_vehiculo_view(request, patente):
    vehiculo = obtener_vehiculo(patente)
    return JsonResponse(
        {
            "patente": vehiculo.patente,
            "marca": vehiculo.marca,
            "modelo": vehiculo.modelo,
            "year": vehiculo.year,
        }
    )


# Vista para obtener la información de un chofer
def obtener_chofer_view(request, rut):
    chofer = obtener_chofer(rut)
    return JsonResponse(
        {
            "rut": chofer.rut,
            "nombre": chofer.nombre,
            "apellido": chofer.apellido,
            "activo": chofer.activo,
            "vehiculo_patente": chofer.vehiculo.patente if chofer.vehiculo else None,
        }
    )


# Vista para asignar un chofer a un vehículo
def asignar_chofer_a_vehiculo_view(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        patente = request.POST.get("patente")
        if rut and patente:
            chofer = asignar_chofer_a_vehiculo(rut, patente)
            return JsonResponse(
                {
                    "chofer": str(chofer),
                    "vehiculo_asignado": (
                        chofer.vehiculo.patente if chofer.vehiculo else None
                    ),
                }
            )
        else:
            return HttpResponseBadRequest(
                "Faltan datos para asignar el chofer al vehículo."
            )
    return HttpResponseBadRequest("Método HTTP no permitido.")


# Vista para imprimir los datos de todos los vehículos
def imprimir_datos_vehiculos_view(request):
    datos = imprimir_datos_vehiculos()
    return JsonResponse({"vehiculos": datos})
