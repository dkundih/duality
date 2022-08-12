### TEST ENV ###
import duality

app = duality.DualityApp()

class Car:

    @app.entry(option_name = 'initialize', option_description = 'starts the car object.')
    def __init__(self, brand = app.store('brand', 'str'), speed = app.store('speed', 'int'), country = app.store('country', 'str')):
        self.brand = brand
        self.speed = speed
        self.country = country

    @app.entry(option_name = 'change speed', option_description = 'this changes the speed of the car.')
    def set_name(self, amount = app.store('amount', 'int')):
        self.speed += amount
        return self.speed

    @app.entry('show info', option_description = 'describes the car.', print_val = True)
    def show_info(self):
        return f'Car of the brand {self.brand}, speed {self.speed} from the country of {self.country}.'

if __name__ == '__main__':
    app.wheel(type = 'dynamic')