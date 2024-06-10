from flask import Flask, request
import requests
import os
import sys

def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

sys.path.append('../../modulo')
import config
from modulo import zph_style

app = Flask(__name__)

@app.route('/')
def index():
    # Hacer una solicitud a un servicio para obtener la IP pública
    response = requests.get('https://api.ipify.org')
    public_ip = response.text
    print()
    zph_style.to_style("LA IP CAPTURADA: ")
    print(public_ip)

    # Obtener la lista de archivos en el directorio 'static'
    static_files = os.listdir('static')

    # Seleccionar solo una imagen de fondo
    background_image = f"/static/{static_files[0]}"

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Background Image</title>
    <style>
        body {{
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-image: url('{background_image}');
            /* Añade otros estilos según sea necesario */
        }}
        /* Estilos adicionales para el contenido */
        .content {{
            text-align: center;
            padding: 50px;
            color: white;
        }}
        /* Añade estilos adicionales según sea necesario */
    </style>
</head>
<body>
    <div class="content">
        <!-- Contenido de tu página aquí -->
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    config.basic()
    app.run(debug=True, port=config.puertos())
