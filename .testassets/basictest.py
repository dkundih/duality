
# EXAMPLE OF USE IN SIMPLE APP CREATION.

from duality import Record

t = Record()

class Queue:

    def __init__(self, dictionary = {}):
        self.dictionary = dictionary
        return

    @t.entry(option_name='zbrajanje')
    def zbrajanje(self):
        x = int(input('Unesi prvi broj: '))
        y = int(input('Unesi drugi broj: '))
        rez = print('Zbroj je: ', x + y)
        return rez

    @t.entry(option_name='oduzimanje')
    def oduzimanje(self):
        x = int(input('Unesi prvi broj: '))
        y = int(input('Unesi drugi broj: '))
        rez = print('Razlika je: ', x - y)
        return rez

    @t.entry(option_name='množenje')
    def množenje(self):
        x = int(input('Unesi prvi broj: '))
        y = int(input('Unesi drugi broj: '))
        rez = print('Umnožak je: ', x * y)
        return rez

    @t.entry(option_name='dijeljenje')
    def dijeljenje(self):
        x = int(input('Unesi prvi broj: '))
        y = int(input('Unesi drugi broj: '))
        rez = print('Produkt je: ', x // y)
        return rez


t.config(queue=True)