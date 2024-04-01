# generar_html_aves.py
from obtener_datos_aves import obtener_datos_aves
from string import Template


def crear_ave_template(ave):
    ave_template = Template(
        """
    <div class="card">
        <img class="card-img" src="$imagen_url_principal" alt="Imagen principal de $nombre_espanol">
        <div class="card-info">
            <h2>$nombre_espanol</h2>
            <h3>$nombre_ingles</h3>
        </div>
    </div>
    """
    )
    return ave_template.substitute(
        nombre_espanol=ave["name"]["spanish"],
        nombre_ingles=ave["name"]["english"],
        imagen_url_principal=ave["images"]["main"],
    )


def generar_html_aves(aves):
    texto_aves = "".join([crear_ave_template(ave) for ave in aves])
    html_template = Template(
        """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Aves de Chile</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; box-sizing: border-box; }
        h1 { text-align: center; color: #007BFF; margin-bottom: 20px; }
        .cards-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; justify-content: center; }
        .card { border: 1px solid #ddd; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.2); transition: transform 0.2s; }
        .card:hover { transform: scale(1.05); }
        .card-img { width: 100%; height: auto; object-fit: contain; background-color: #f8f9fa; }
        .card-info { padding: 15px; text-align: center; }
        h2, h3 { margin: 5px 0; }
    </style>
    </head>
    <body>
    <h1>Aves de Chile</h1>
    <div class="cards-container">
        $body
    </div>
    </body>
    </html>
    """
    )
    return html_template.substitute(body=texto_aves)


if __name__ == "__main__":
    aves = obtener_datos_aves()
    html_content = generar_html_aves(aves)
    with open("aves_de_chile.html", "w", encoding="utf-8") as file:
        file.write(html_content)
