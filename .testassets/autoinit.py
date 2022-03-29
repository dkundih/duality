
# MISC PARTICLES AND A TEST FIELD.

class One:

    def __init__(self, text, number):
        print(text, number)

class Two:

    def __init__(self, func, func_args):
        func(**func_args)

Two(One, func_args = {'text': 'Hello', 'number': 1})

def autoinit(self, func, func_args = {}):

    try:
        if func_args == {}:
            
            return func(self)
        else:
            return func(self, **func_args)

    except:
        if func_args == {}:

            return func()
        else:
            return func(**func_args)