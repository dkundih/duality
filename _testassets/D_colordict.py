
# MISC PARTICLES AND A TEST FIELD.

from colorama import (
    Fore,
    init,
)

init()

def paint_text(text, color, print_trigger = True):
    colors = {'r': Fore.RED,
              'g' : Fore.GREEN,
              'b' : Fore.BLUE,
              'k' : Fore.BLACK,
              'm' : Fore.MAGENTA,
              'y' : Fore.YELLOW,
              'c' : Fore.CYAN,
              }
    if print_trigger == True:
        return print(colors[color] + text + Fore.RESET)
    
    elif print_trigger == False:
        return colors[color] + text + Fore.RESET
        
paint_text('tekst', 'g')
