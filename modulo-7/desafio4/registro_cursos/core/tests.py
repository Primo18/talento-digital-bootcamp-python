from django.test import TestCase
from .models import Estudiante, Profesor, Curso, Direccion
from .services import (
    crear_curso,
    crear_profesor,
    crear_estudiante,
    crear_direccion,
    obtiene_estudiante,
    obtiene_profesor,
    obtiene_curso,
    agrega_profesor_a_curso,
    agrega_cursos_a_estudiante,
    imprime_estudiante_cursos,
)


class ServicesTestCase(TestCase):

    def setUp(self):
        # Crea datos de prueba
        self.profesor = crear_profesor(
            rut="123456789", nombre="John", apellido="Doe", creado_por="admin"
        )
        self.estudiante = crear_estudiante(
            rut="987654321",
            nombre="Jane",
            apellido="Smith",
            fecha_nac="2000-01-01",
            creado_por="admin",
        )
        self.curso = crear_curso(
            codigo="CS101",
            nombre="Introducción a la Programación",
            version=1,
            profesor_rut=self.profesor.rut,
        )

    def test_crear_curso(self):
        curso = crear_curso(codigo="CS102", nombre="Estructuras de Datos", version=1)
        self.assertEqual(curso.codigo, "CS102")
        self.assertEqual(curso.nombre, "Estructuras de Datos")
        self.assertEqual(curso.version, 1)
        self.assertIsNone(curso.profesor)

    def test_agrega_cursos_a_estudiante(self):
        agrega_cursos_a_estudiante(
            estudiante_rut=self.estudiante.rut, cursos_codigos=[self.curso.codigo]
        )
        cursos = self.estudiante.cursos.all()
        self.assertEqual(cursos.count(), 1)
        self.assertEqual(cursos.first().codigo, self.curso.codigo)

    def test_imprime_estudiante_cursos(self):
        agrega_cursos_a_estudiante(
            estudiante_rut=self.estudiante.rut, cursos_codigos=[self.curso.codigo]
        )
        cursos = imprime_estudiante_cursos(estudiante_rut=self.estudiante.rut)
        self.assertEqual(len(cursos), 1)
        self.assertEqual(cursos[0].codigo, self.curso.codigo)

    def test_obtiene_estudiante(self):
        estudiante = obtiene_estudiante(rut=self.estudiante.rut)
        self.assertIsNotNone(estudiante)
        self.assertEqual(estudiante.rut, self.estudiante.rut)

    def test_obtiene_profesor(self):
        profesor = obtiene_profesor(rut=self.profesor.rut)
        self.assertIsNotNone(profesor)
        self.assertEqual(profesor.rut, self.profesor.rut)

    def test_obtiene_curso(self):
        curso = obtiene_curso(codigo=self.curso.codigo)
        self.assertIsNotNone(curso)
        self.assertEqual(curso.codigo, self.curso.codigo)

    def test_agrega_profesor_a_curso(self):
        profesor = crear_profesor(
            rut="987654322", nombre="Jane", apellido="Smith", creado_por="admin"
        )
        agrega_profesor_a_curso(
            codigo_curso=self.curso.codigo, rut_profesor=profesor.rut
        )
        curso = Curso.objects.get(codigo=self.curso.codigo)
        self.assertEqual(curso.profesor.rut, profesor.rut)

    def test_crear_profesor(self):
        profesor = crear_profesor(
            rut="987654322", nombre="Jane", apellido="Smith", creado_por="admin"
        )
        self.assertEqual(profesor.rut, "987654322")
        self.assertEqual(profesor.nombre, "Jane")
        self.assertEqual(profesor.apellido, "Smith")
        self.assertFalse(
            profesor.activo
        )  # Verifica que el valor por defecto de activo sea False

    def test_crear_estudiante(self):
        estudiante = crear_estudiante(
            rut="987654322",
            nombre="Jane",
            apellido="Smith",
            fecha_nac="2000-01-01",
            creado_por="admin",
        )
        self.assertEqual(estudiante.rut, "987654322")
        self.assertEqual(estudiante.nombre, "Jane")
        self.assertEqual(estudiante.apellido, "Smith")
        self.assertEqual(estudiante.fecha_nac, "2000-01-01")
        self.assertFalse(
            estudiante.activo
        )  # Verifica que el valor por defecto de activo sea False

    def test_crear_direccion(self):
        direccion = crear_direccion(
            calle="Calle Falsa",
            numero="123",
            comuna="Springfield",
            ciudad="Springfield",
            region="Región Metropolitana",
            estudiante_rut=self.estudiante.rut,
        )
        self.assertEqual(direccion.calle, "Calle Falsa")
        self.assertEqual(direccion.numero, "123")
        self.assertEqual(direccion.comuna, "Springfield")
        self.assertEqual(direccion.ciudad, "Springfield")
        self.assertEqual(direccion.region, "Región Metropolitana")
        self.assertEqual(direccion.estudiante.rut, self.estudiante.rut)
        self.assertIsNone(
            direccion.dpto
        )  # Verifica que dpto es None cuando no se proporciona
