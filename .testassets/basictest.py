
# EXAMPLE OF USE IN SIMPLE APP CREATION.

import duality

print(duality.__version__,'\n')

t = duality.Record()

class App:

    @t.entry(option_name='init', autoinit=True)
    def __init__(self, dictionary = {}):
        self.dictionary = dictionary
        return

    @t.entry(option_name='zbrajanje')
    def zbrajanje(self, x = t.store('x', 'float',), y = t.store('y', 'float')):
        rez = print('Zbroj je: ', x + y)
        return rez

    @t.entry(option_name='oduzimanje')
    def oduzimanje(self, x = t.store('x', 'int') , y = t.store('y', 'int')):
        rez = print('Razlika je: ', x - y)
        return rez

    def initconfig(self):
        t.config(type = 'dynamic', queue=True)

a = App()

if __name__ == '__main__':
    a.initconfig()