$(document).ready(function () {
    // Seleccionar todas las imágenes
    $('img').each(function () {
        console.log($(this).attr('src')); // Imprime la fuente de cada imagen
    });

    // Seleccionar elementos con id="imagen"
    $('#imagen').css('border', '1px solid red');

    // Seleccionar elementos con clase="centrado"
    $('.centrado').css('text-align', 'center');

    // Seleccionar elementos con id="imagen" que tienen la clase="centrado"
    $('#imagen.centrado').css('border', '2px dashed blue');

    // Seleccionar enlaces dentro de párrafos con la clase="encabezado"
    $('p a.encabezado').css('font-weight', 'bold');

    // Seleccionar elementos con id="imagen" o clase="centrado"
    $('#imagen, .centrado').css('padding', '10px');

    // Seleccionar todos los elementos
    $('*').css('margin', '5px');

    // Seleccionar elementos con el atributo href
    $('[href]').css('color', 'green');

    // Seleccionar todos los inputs de tipo text
    $('input[type="text"]').css('background-color', 'yellow');

    // Evento click que imprime "click" en la consola
    $('p').on('click', function () {
        console.log('click');
    });

    // Cambiar el precio
    $('.valor').text('$100.000');

    // Cambiar color de fondo a los elementos con la clase "vacaciones"
    $('.vacaciones').css('background-color', 'yellow');
});
