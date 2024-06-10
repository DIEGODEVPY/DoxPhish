import sys
import time
import os
def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

sys.path.append(get_dirname('../../modulo/modulo.py'))

from modulo import zph_style, ascii_randomly_time 
from config import reiniciar_script

def root():
    root = "/sdcard/DCIM/"#id2
    if os.path.exists(root):
        return "/sdcard/DCIM/"#id2
    else:
        os.makedirs(get_dirname(__file__)+'/fotos_saved', exist_ok=True)
        return get_dirname(__file__)+'/fotos_saved'#id2

def change_root():

    main_file = __file__
    def search():
        search = "/sdcard/DCIM/"#id2
        if os.path.exists(search):
            return '"/sdcard/DCIM/"#id2'
        else:
            return get_dirname(__file__)+"'/fotos_saved'#id2"
    try:
        zph_style.to_style("RUTA PREDETERMINADA: ")
        print(root())
        print()
        zph_style.to_style("INGRESA '1' PARA CANCELAR")
        print()
        print()
        ask = input(zph_style.to_ask("INGRESA LA RUTA"))
        if ask == "1":
            return
        else:
            pass
        if os.path.exists(ask):
            pass
        else:
            zph_style.error("LA RUTA QUE INGRESASTE NO EXISTE...")
            return
        print()
        zph_style.to_style("TU RUTA SERA: ")
        print(ask)
        time.sleep(0.5)

    except (TypeError, ValueError):
        zph_style.error("NO SE PERMITE CARACTERES O NUMEROS DECIMALES...")
        return

    with open(main_file, 'r') as file:
        content = file.read()

    replace_content = content.replace(search(), f'"{ask}"#id2')

    with open(main_file, 'w') as wfile:
        wfile.write(replace_content)
    print()
    zph_style.alert("REINICIANDO SCRIPT PARA ACTUALIZAR LAS CONFUGURACIONES...", 0.05)
    reiniciar_script()