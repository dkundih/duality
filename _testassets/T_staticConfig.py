### TEST ENV ###
import duality

t = duality.DualityApp()

class App:

    @t.entry(option_name = 'zbrajanje', option_description = 'zbraja vrijednosti.', print_val = True)
    def zbrajanje(x = t.store('x', 'float',), y = t.store('y', 'float')):
        rez = 'Zbroj je: ', x + y
        return rez

    @t.entry(option_name = 'oduzimanje', option_description = 'oduzima vrijednosti.', print_val = True)
    def oduzimanje(x = t.store('x', 'int') , y = t.store('y', 'int')):
        rez = 'Razlika je: ', x - y
        return rez

    def initconfig(self):
        t.config(type = 'static', queue = True)

a = App()

if __name__ == '__main__':
    a.initconfig()