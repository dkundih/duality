
# EXAMPLE OF USE IN SIMPLE APP CREATION.

from duality import Record

t = Record()

class App:

    @t.entry(option_name='init', autoinit=True)
    def __init__(self, dictionary = {}):
        self.dictionary = dictionary
        return

    @t.entry(option_name='zbrajanje')
    def zbrajanje(self):
        x = t.define(input_val = 'x', dtype = 'int')
        y = t.define(input_val = 'y', dtype = 'int')
        rez = print('Zbroj je: ', x + y)
        return rez

    @t.entry(option_name='oduzimanje')
    def oduzimanje(self):
        x = t.define(input_val = 'x', dtype = 'int')
        y = t.define(input_val = 'y', dtype = 'int')
        rez = print('Razlika je: ', x - y)
        return rez

    @t.entry(option_name='množenje')
    def množenje(self):
        x = t.define(input_val = 'x', dtype = 'int')
        y = t.define(input_val = 'y', dtype = 'int')
        rez = print('Umnožak je: ', x * y)
        return rez

    @t.entry(option_name='dijeljenje')
    def dijeljenje(self):
        x = t.define(input_val = 'x', dtype = 'int')
        y = t.define(input_val = 'y', dtype = 'int')
        rez = print('Produkt je: ', x // y)
        return rez

    def initconfig(self):
        t.config(type = 'dynamic', queue=True)

a = App()

a.initconfig()