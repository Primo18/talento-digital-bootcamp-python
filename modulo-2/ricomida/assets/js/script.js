$(document).ready(function () {
    // Carousel: Ocultar en tamaños sm y xs
    function checkCarouselDisplay() {
        if ($(window).width() < 768) {
            $('#recipeCarousel').hide();
        } else {
            $('#recipeCarousel').show();
        }
    }

    checkCarouselDisplay(); // Ejecutar al cargar
    $(window).resize(checkCarouselDisplay); // Ejecutar en el evento resize

    // Tooltip para el botón de enviar por correo
    $('#enviarCorreo').tooltip();

    // Evento click para el botón de enviar por correo
    $('#enviarCorreo').on('click', function () {
        alert('El correo fue enviado correctamente...');
    });

    // Selectores de etiqueta y dblclick
    $('h2').on('dblclick', function () {
        $(this).css('color', 'red');
    });

    // // Selectores de clase y toggle
    // $('.card-title').on('click', function () {
    //     $(this).next('.card-text').toggle();
    // });

    $('.related-recipes .card-title').on('click', function () {
        // Aquí usamos .closest('.card') para asegurarnos de afectar solo al contenido de la tarjeta en la que se hizo clic
        // y luego encontramos todos los .card-text dentro de la sección de Recetas Relacionadas para aplicarles toggle.
        $(this).closest('.related-recipes').find('.card-text').toggle();
    });
});

