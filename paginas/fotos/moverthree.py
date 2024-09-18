import os
import shutil
import itertools
import os
import sys

def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

sys.path.append(get_dirname('../../modulo/modulo.py'))

from modulo import zph_style
from config import openfile, reiniciar_script

def borrar_archivos_en_directorio(ruta_directorio):
    elementos = os.listdir(ruta_directorio)
    for elemento in elementos:
        ruta_elemento = os.path.join(ruta_directorio, elemento)
        if os.path.isfile(ruta_elemento):
            os.remove(ruta_elemento)
        else:
            print("")

directorio_a_limpiar = get_dirname(__file__)+'/static/'


def renombrar_archivo(ruta_original, nuevo_nombre):

    extension = os.path.splitext(ruta_original)[1]

    nueva_ruta = os.path.join(os.path.dirname(ruta_original), nuevo_nombre + extension)

    os.rename(ruta_original, nueva_ruta)

def process_imagethree(Value = False):
    extensions = ('.jpeg', '.jpg', '.png', '.gif', '.svg', '.webp', '.bmp')

    zph_style.to_style("ASEGURATE QUE LA IMAGEN TENGA UNA ESCALA COMPATIBLE")
    print()
    print()
    zph_style.to_style("IMAGEN PREDETERMINADO: ")
    print("/storage/emulated/0/Download/earth-11015-1920-41.jpg")#id1
    print()
    ask_ruta = input(zph_style.to_ask("INGRESA LA RUTA DEL IMAGEN"))

    if os.path.isfile(ask_ruta) and ask_ruta.lower().endswith(extensions):
        print()
        zph_style.to_style("IMAGEN VALIDA")
        borrar_archivos_en_directorio(directorio_a_limpiar)
        dir_file = os.path.dirname(ask_ruta)
        base_file = os.path.basename(ask_ruta)
        imgs = f'imagen'
        shutil.copy(ask_ruta, get_dirname(__file__)+'/static')
        renombrar_archivo(get_dirname(__file__)+'/static/' + base_file, imgs)
        openfile(__file__, 'print("/storage/emulated/0/Download/earth-11015-1920-41.jpg")#id1', f'print("{ask_ruta}")#id1')
        print()
        zph_style.alert("REINICIANDO PARA GUARDAR CAMBIOS...", 0.02)
        reiniciar_script()

    else:
        zph_style.error("LA IMAGEN ES INVALIDA O NO EXISTE...")
