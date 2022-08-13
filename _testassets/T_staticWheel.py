### TEST ENV ###
import duality
import time
from logistics.plugins.coloring import paint_text

app = duality.DualityApp()

class Car:

    @app.entry(option_name = 'change speed', option_description = 'this changes the speed of the car.', print_val = True)
    def set_name(speed = 0, amount = app.store('amount', 'int')):
        speed += amount
        return speed

    @app.entry('show info', option_description = 'describes the car.', print_val = True)
    def show_info():
        return 'This would show some text in general.'

if __name__ == '__main__':
    paint_text(text = '\n>>> Executed on: ' + str(duality.__version__) + ' <<<', color = 'Fy', print_trigger = True)
    time.sleep(3)
    app.wheel(type = 'static')
