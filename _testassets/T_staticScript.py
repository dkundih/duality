### TEST ENV ###
import duality
import time
from logistics.plugins.coloring import paint_text

app = duality.DualityApp()

class App:

    @app.entry(option_name = 'add', option_description = 'adds values.', print_val = True)
    def zbrajanje(x = app.store('x', 'float', 'FIRST NUMBER'), y = app.store('y', 'float', 'SECOND NUMBER')):
        rez = x + y
        return rez

    @app.entry(option_name = 'subtract', option_description = 'subtracts values.', print_val = True)
    def oduzimanje(x = app.store('x', 'int', 'FIRST NUMBER') , y = app.store('y', 'int', 'SECOND NUMBER')):
        rez = x - y
        return rez

if __name__ == '__main__':
    paint_text(text = '\n>>> Executed on: ' + str(duality.__version__) + ' <<<', color = 'Fy', print_trigger = True)
    time.sleep(3)
    app.script(type = 'static')
