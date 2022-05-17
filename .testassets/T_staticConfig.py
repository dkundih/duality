
# EXAMPLE OF USE IN SIMPLE APP CREATION USING STATIC CONFIG.

import duality

print(duality.__version__,'\n')

t = duality.Record()

@t.entry(option_name='zbrajanje')
def zbrajanje(x = t.store('x', 'float',), y = t.store('y', 'float')):
    rez = print('Zbroj je: ', x + y)
    return rez

@t.entry(option_name='oduzimanje')
def oduzimanje(x = t.store('x', 'int') , y = t.store('y', 'int')):
    rez = print('Razlika je: ', x - y)
    return rez

def initconfig():
    t.config(type = 'static', queue=True)

if __name__ == '__main__':
    initconfig()