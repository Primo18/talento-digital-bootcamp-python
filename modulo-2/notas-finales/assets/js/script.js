// Uso de const para elementos que no cambian
const nombre = document.getElementById("nombre");
const carrera = document.getElementById("carrera");

// Función para solicitar datos al usuario y asignarlos a elementos HTML
const solicitarYMostrarDatos = (mensaje, elemento) => {
    const dato = prompt(mensaje, "");
    if (dato !== null) elemento.textContent = dato;
};

solicitarYMostrarDatos("Ingresa tu nombre", nombre);
solicitarYMostrarDatos("Ingresa tu carrera", carrera);

// Función para calcular y mostrar las notas y promedios
const calcularYMostrarNotas = (asignatura) => {
    const nota1 = +prompt(`Ingrese nota 1 [${asignatura}]`, "");
    const nota2 = +prompt(`Ingrese nota 2 [${asignatura}]`, "");
    const nota3 = +prompt(`Ingrese nota 3 [${asignatura}]`, "");
    const promedio = ((nota1 + nota2 + nota3) / 3).toFixed(2);

    document.getElementById(`nota1${asignatura}`).textContent = nota1;
    document.getElementById(`nota2${asignatura}`).textContent = nota2;
    document.getElementById(`nota3${asignatura}`).textContent = nota3;
    document.getElementById(`promedio${asignatura}`).textContent = promedio;

    return promedio;
};

const promHTML = calcularYMostrarNotas("HTML");
const promCSS = calcularYMostrarNotas("CSS");
const promJS = calcularYMostrarNotas("JS");

const promFinal = ((parseFloat(promHTML) + parseFloat(promCSS) + parseFloat(promJS)) / 3).toFixed(2);
document.getElementById("promFinal").textContent = promFinal;
