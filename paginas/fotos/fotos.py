from flask import Flask, render_template, Response, request
import os
import base64
from datetime import datetime  # Importar datetime
import sys
import config_fotos

def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

sys.path.append(get_dirname('../../modulo/config.py'))
from config import basic, puertos

app = Flask(__name__)

# Directorio para guardar las fotos
SAVE_DIR = config_fotos.root()

# Ruta principal que muestra el formulario HTML
@app.route('/')
def index():
    static_files = os.listdir('static')
    background_image = f"/static/{static_files[0]}"
    return render_template('index.html', background_image=background_image)

# Ruta para manejar la solicitud de captura de foto
@app.route('/capture', methods=['POST'])
def capture():
    # Obtener el dato de imagen en base64 desde la solicitud
    image_data = request.form['imageData']
    
    # Decodificar el dato de imagen base64 y guardar la foto en un archivo
    if image_data:
        # Crear el directorio para guardar las imágenes si no existe
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
        
        # Guardar la imagen en un archivo
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        image_path = os.path.join(SAVE_DIR, f"photo_{timestamp}.png")
        print("GUARDADO EN: ",SAVE_DIR)
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(image_data.split(',')[1]))
        return "Foto guardada correctamente"
    else:
        return "No se recibió ningún dato de imagen"

if __name__ == '__main__':
    basic()
    app.run(debug=True, port=puertos())
