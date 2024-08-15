from .models import Curso, Profesor, Estudiante, Direccion


def crear_curso(codigo, nombre, version, profesor_rut=None):
    """
    Crea un curso en la base de datos.
    Si se proporciona el rut de un profesor, se asigna al curso.
    """
    if profesor_rut:
        profesor = Profesor.objects.get(rut=profesor_rut)
    else:
        profesor = None
    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, version=version, profesor=profesor
    )
    return curso


def crear_profesor(rut, nombre, apellido, activo=False, creado_por=""):
    """
    Crea un profesor en la base de datos.
    """
    profesor = Profesor.objects.create(
        rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por
    )
    return profesor


def crear_estudiante(rut, nombre, apellido, fecha_nac, activo=False, creado_por=""):
    """
    Crea un estudiante en la base de datos.
    """
    estudiante = Estudiante.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac,
        activo=activo,
        creado_por=creado_por,
    )
    return estudiante


def crear_direccion(calle, numero, comuna, ciudad, region, estudiante_rut, dpto=None):
    """
    Crea una dirección para un estudiante específico.
    """
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    direccion = Direccion.objects.create(
        calle=calle,
        numero=numero,
        comuna=comuna,
        ciudad=ciudad,
        region=region,
        estudiante=estudiante,
        dpto=dpto,
    )
    return direccion


def obtiene_estudiante(rut):
    """
    Obtiene un estudiante por su rut.
    """
    try:
        estudiante = Estudiante.objects.get(rut=rut)
        return estudiante
    except Estudiante.DoesNotExist:
        return None


def obtiene_profesor(rut):
    """
    Obtiene un profesor por su rut.
    """
    try:
        profesor = Profesor.objects.get(rut=rut)
        return profesor
    except Profesor.DoesNotExist:
        return None


def obtiene_curso(codigo):
    """
    Obtiene un curso por su código.
    """
    try:
        curso = Curso.objects.get(codigo=codigo)
        return curso
    except Curso.DoesNotExist:
        return None


def agrega_profesor_a_curso(codigo_curso, rut_profesor):
    """
    Asigna un profesor a un curso existente.
    """
    curso = Curso.objects.get(codigo=codigo_curso)
    profesor = Profesor.objects.get(rut=rut_profesor)
    curso.profesor = profesor
    curso.save()
    return curso


def agrega_cursos_a_estudiante(estudiante_rut, cursos_codigos):
    """
    Asocia uno o más cursos a un estudiante.
    """
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    cursos = Curso.objects.filter(codigo__in=cursos_codigos)
    estudiante.cursos.add(*cursos)
    return estudiante


def imprime_estudiante_cursos(estudiante_rut):
    """
    Imprime y retorna todos los cursos en los que está inscrito un estudiante.
    """
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    cursos = estudiante.cursos.all()
    for curso in cursos:
        print(f"Curso: {curso.nombre} (Código: {curso.codigo})")
    return cursos
