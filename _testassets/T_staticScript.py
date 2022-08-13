### TEST ENV ###
import duality
import time
from logistics.plugins.coloring import paint_text

app = duality.DualityApp()

class App:

    @app.entry(option_name = 'zbrajanje', option_description = 'zbraja vrijednosti.')
    def zbrajanje(x = app.store('x', 'float',), y = app.store('y', 'float')):
        rez = x + y
        return print('Zbroj je:', rez)

    @app.entry(option_name = 'oduzimanje', option_description = 'oduzima vrijednosti.')
    def oduzimanje(x = app.store('x', 'int') , y = app.store('y', 'int')):
        rez = x - y
        return print('Razlika je:', rez)

if __name__ == '__main__':
    paint_text(text = '\n>>> Executed on: ' + str(duality.__version__) + ' <<<', color = 'Fy', print_trigger = True)
    time.sleep(3)
    app.script(type = 'static')
