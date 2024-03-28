preguntas_basicas = {
    "pregunta_1": {
        "enunciado": ["¿Qué es Python?"],
        "alternativas": [
            ["Un juego de computadora", 0],
            ["Un lenguaje de programación", 1],
            ["Una serpiente", 0],
            ["Una herramienta de cocina", 0],
        ],
    },
    "pregunta_2": {
        "enunciado": ["¿Para qué se usa la función print()?"],
        "alternativas": [
            ["Para sumar números", 0],
            ["Para imprimir mensajes en la pantalla", 1],
            ["Para leer archivos", 0],
            ["Para crear variables", 0],
        ],
    },
    "pregunta_3": {
        "enunciado": ["¿Qué tipo de lenguaje es Python?"],
        "alternativas": [
            ["De bajo nivel", 0],
            ["De marcado", 0],
            ["Interpretado", 1],
            ["Compilado", 0],
        ],
    },
}

preguntas_intermedias = {
    "pregunta_1": {
        "enunciado": [
            "¿Qué estructura de datos no permite elementos duplicados en Python?"
        ],
        "alternativas": [
            ["Lista", 0],
            ["Conjunto", 1],
            ["Diccionario", 0],
            ["Tupla", 0],
        ],
    },
    "pregunta_2": {
        "enunciado": ['¿Qué significa que una función sea "idempotente"?'],
        "alternativas": [
            ["Que puede cambiar objetos mutables", 0],
            ["Que siempre devuelve el mismo resultado para los mismos argumentos", 1],
            ["Que incrementa automáticamente los valores", 0],
            ["Que no retorna ningún valor", 0],
        ],
    },
    "pregunta_3": {
        "enunciado": ["¿Qué operador se usa para la división entera?"],
        "alternativas": [["/", 0], ["%", 0], ["//", 1], ["**", 0]],
    },
}

preguntas_avanzadas = {
    "pregunta_1": {
        "enunciado": ["¿Qué hace el decorador @staticmethod?"],
        "alternativas": [
            ["Hace que un método de instancia no requiera un argumento self", 0],
            ["Convierte una función en un método estático de una clase", 1],
            ["Crea una copia estática de una variable", 0],
            ["Ninguna de las anteriores", 0],
        ],
    },
    "pregunta_2": {
        "enunciado": ["¿Cuál es la diferencia principal entre __str__ y __repr__?"],
        "alternativas": [
            [
                "__str__ es usado por print(), __repr__ para todas las demás representaciones",
                1,
            ],
            ["__repr__ es usado por print(), __str__ no se usa", 0],
            ["__str__ no se puede sobrecargar, __repr__ sí", 0],
            ["No hay diferencia", 0],
        ],
    },
    "pregunta_3": {
        "enunciado": ["¿Qué es la Programación Orientada a Aspectos?"],
        "alternativas": [
            ["Un paradigma de programación basado en clases", 0],
            ["Programación que se enfoca exclusivamente en la seguridad", 0],
            [
                "Un enfoque que permite la separación de preocupaciones en el software",
                1,
            ],
            ["Ninguna de las anteriores", 0],
        ],
    },
}

pool_preguntas = {
    "basicas": preguntas_basicas,
    "intermedias": preguntas_intermedias,
    "avanzadas": preguntas_avanzadas,
}
