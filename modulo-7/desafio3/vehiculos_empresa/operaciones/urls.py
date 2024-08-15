from django.urls import path
from . import views

urlpatterns = [
    path("crear-vehiculo/", views.crear_vehiculo_view, name="crear_vehiculo"),
    path("crear-chofer/", views.crear_chofer_view, name="crear_chofer"),
    path(
        "crear-registro-contable/",
        views.crear_registro_contable_view,
        name="crear_registro_contable",
    ),
    path(
        "deshabilitar-chofer/<str:rut>/",
        views.deshabilitar_chofer_view,
        name="deshabilitar_chofer",
    ),
    path(
        "deshabilitar-vehiculo/<str:patente>/",
        views.deshabilitar_vehiculo_view,
        name="deshabilitar_vehiculo",
    ),
    path(
        "habilitar-chofer/<str:rut>/",
        views.habilitar_chofer_view,
        name="habilitar_chofer",
    ),
    path(
        "habilitar-vehiculo/<str:patente>/",
        views.habilitar_vehiculo_view,
        name="habilitar_vehiculo",
    ),
    path(
        "vehiculo/<str:patente>/", views.obtener_vehiculo_view, name="obtener_vehiculo"
    ),
    path("chofer/<str:rut>/", views.obtener_chofer_view, name="obtener_chofer"),
    path(
        "asignar-chofer/", views.asignar_chofer_a_vehiculo_view, name="asignar_chofer"
    ),
    path(
        "imprimir-vehiculos/",
        views.imprimir_datos_vehiculos_view,
        name="imprimir_vehiculos",
    ),
]
