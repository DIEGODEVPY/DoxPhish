#ESTO ES UN MODULO QUE SERA USADO POR OTROS SCRIPTS
import random
import os
import time
import logging

try:
    import pystyle
except ModuleNotFoundError:
    os.system("pip install pystyle")

import pystyle

#colores
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
cyan = "\033[95m"
purple = "\033[96m"
cy = "\033[46m"
wh = "\033[47m"
reset = "\033[0m"

def box(texto, space, wait=None):
    c_r = random.choice((red, green, yellow, blue, cyan,purple))
    box_top = c_r + " " * space +"╔" + "═" * (len(texto) + 2) + "╗\n"
    box_middle = " " * space +f"║ {texto} {c_r}║\n"
    box_bottom = " " * space +"╚" + "═" * (len(texto) + 2) + "╝" + reset
    
    def slept():
        slepts = time.sleep(wait)
        return slepts
    for i in box_top:
        print(i, end='',flush=True)
        if wait:
            slept()
    for i in box_middle:
        print(i, end='',flush=True)
        if wait:
            slept()
    for i in box_bottom:
        print(i, end='',flush=True)
        if wait:
            slept()

def ask_seconds_fotos():
    try:
        asking = int(input(zph_style.to_ask("INGRESA LOS SEGUNDOS PARA LA AUTOCAPTURA")))
        print()
        return asking
        ascii_randomly_time(f"AHORA LAS FOTOS SE CAPTURARAN AUTOMATICAMENTE CADA: {asking} SEGUNDOS", 0.04)
    except (ValueError, TypeError):
        zph_style.error("NO CARACTERES NI DECIMALES")

def to_colorate_randomly():
    colorear_random = random.choice((red, green, yellow, blue, cyan,purple))

class zph_style:
    colorate_randomly = random.choice((red, green, yellow, blue, cyan,purple))

    def to_ask(char):
        caracter = f"{yellow} [{reset}?{yellow}] {char} >> {reset}"
        return caracter
        print(caracter, end="", flush=True)
    def error(char):
        caracters = f"{red} [{reset}!{red}] {char}"
        for i in caracters:     
            print(i, end="", flush=True)
            time.sleep(0.01)
    def alert(char,tiempo):
        caracters = f"{yellow} [{red}!{yellow}] {char}"
        for i in caracters:
            print(i, end="", flush=True)
            time.sleep(tiempo)
    def to_style(char):
        co_ra = random.choice((green, blue, cyan,purple))
        caracters = f" {co_ra}[{reset}+{co_ra}] {char}{reset}"
        for i in caracters:
            print(i, end="", flush=True)
            time.sleep(0.02)

def colorate(char):
    colors_list = [
            pystyle.Colors.red_to_blue,
            pystyle.Colors.red_to_green,
            pystyle.Colors.blue_to_green,
            pystyle.Colors.yellow_to_red
            ]
    choose_randomly = random.choice(colors_list)
    chose = pystyle.Colorate.Horizontal(choose_randomly,char)
    for i in chose:
        print(i, end="", flush=True)

def colorate_time(char):
    colors_list = [
        pystyle.Colors.red_to_blue,
        pystyle.Colors.red_to_green,
        pystyle.Colors.blue_to_green
    ]
    choose_randomly = random.choice(colors_list)
    chose = pystyle.Colorate.Horizontal(choose_randomly, char)
    for i in chose:
        print(i, end="", flush=True)  
        time.sleep(0.00001)

def ascii_randomly(char):
    colorate_randomly = random.choice((red, green, yellow, blue, cyan,purple))
    print(colorate_randomly+char+reset, end="", flush=True)

def ascii_randomly_time(char, slept):
    colorate_randomly = random.choice((red, green, yellow, blue, cyan,purple))
    colorated = colorate_randomly+char+reset
    for i in colorated:
        print(i, end="", flush=True)
        time.sleep(slept)

class main_head:

    def text_banner():
        t_b1 = f"""
  _____            _____  _     _     _     
 |  __ \          |  __ \| |   (_)   | |    
 | |  | | _____  _| |__) | |__  _ ___| |__  
 | |  | |/ _ \ \/ /  ___/| '_ \| / __| '_ \ 
 | |__| | (_) >  <| |    | | | | \__ \ | | |
 |_____/ \___/_/\_\_|    |_| |_|_|___/_| |_|
"""

        t_b2 = """
 ___                 ___    _               _     
(  _`\              (  _`\ ( )     _       ( )    
| | ) |   _         | |_) )| |__  (_)  ___ | |__  
| | | ) /'_`\ (`\/')| ,__/'|  _ `\| |/',__)|  _ `\ 
| |_) |( (_) ) >  < | |    | | | || |\__, \| | | |
(____/'`\___/'(_/\_)(_)    (_) (_)(_)(____/(_) (_)
"""
        t_b3 = """
________             ______________ _____       ______  
___  __ \_________  ____  __ \__  /____(_)_________  /_ 
__  / / /  __ \_  |/_/_  /_/ /_  __ \_  /__  ___/_  __ \ 
_  /_/ // /_/ /_>  < _  ____/_  / / /  / _(__  )_  / / /
/_____/ \____//_/|_| /_/     /_/ /_//_/  /____/ /_/ /_/ 
"""

        t_b = random.choice((t_b1, t_b2, t_b3))
        colorate(t_b)

    def logo_banner():
        
        l_b1 = f"""
                ______      ___
         /\  _/  /  __ \    \  \ 
        /\ \/   |    0\ |   |  |
       /\_/     \     __/   |  |
       \/         \___\     |  |
       /   /   /   _)   •   |  |
       |  / /_/  _) \   /\__/  /
    ___|  \/   _)\ \/   \_____/
    \    ____/    \/
     \   )
      \ /
"""
        
        l_b2 = f"""
               ________   _____
      ________/  /  /  / /     |
    /   ___            \/   ___|
   /   (@)                     |
  |             __             |
  |___         <__)         ___|
     /      (       (    /\    |
     \_______\       \__/  \___|
              \_______\ 
"""
        l_b3 = """

      /`·.¸             ,--.. 
     /¸...¸`:·         .''-..'
 ¸.·´  ¸   `·.¸.·´)   /@    `.-:  
: © ):´;      ¸  {    > )<  ,-.:
 `·.¸ `·  ¸.·´\`·¸)   `..-',:-
     ```´´\¸.·´          `-'

"""
        logob = random.choice((l_b1, l_b2, l_b3))
        ascii_randomly(logob)
    def author_text():
        c_r = random.choice((red, green, yellow, blue, cyan,purple))
        texto = "CREADO POR DIEGO.DEV"
        box_top = "      ╔" + "═" * (len(texto) + 2) + "╗"
        box_middle = f"      ║ {reset}{texto} {c_r}║"
        box_bottom = "      ╚" + "═" * (len(texto) + 2) + "╝"
    
        print(c_r+box_top)
        print(c_r+box_middle)
        print(c_r+box_bottom+reset)

    def message_exit():
        print()
        for i in f" {yellow}Ctrl+C para salir{reset}\n":
            print(i, end="", flush=True)
            time.sleep(0.01)

