# stores menu options over functions and class methods and lists all options.
class record:
    menu = []

    def __init__(self, func):
        self.func = func

    def entry(name):
        def wrapper(func):
            def decorator( *args, **kwargs):
                record.menu += [name]
                return func(*args, **kwargs)
            return decorator
        return wrapper

    def display(method = 'return'):
        if method == 'return':
            def wrapper(func):
                def decorator(*args, **kwargs):
                    return record.menu
                return decorator
            return wrapper
        elif method == 'listed':
            def wrapper(func):
                def decorator(*args, **kwargs):
                    for i in record.menu:
                        print(i)
                return decorator
            return wrapper

# tracks function behaviuor and stores it into a JSON file.
class track:
    def entry(func_name):
        def log(func):
                import sys
                import json
                import datetime
                def logsaver(*args, **kwargs):
                    start = datetime.datetime.now()
                    results = func(*args, **kwargs)
                    end = datetime.datetime.now()
                    data = {
                        'insight' : [
                                {
                                    'FUNCTION NAME: ' : func_name,
                                    'EXECUTION TIME: ' : str(end - start),
                                    'EXECUTED AT: ' : str(datetime.datetime.now()),
                                    'MEMORY SIZE: ' : str(sys.getsizeof(func)) + ' bytes',
                                }
                            ]
                        }
                    with open('Logs.json', 'a') as f:
                        f.write(json.dumps(data, indent=4))
                        return results
                return logsaver
        return log

    def display():
        f = open('Logs.json', 'r')
        print(f.read())

'''
@track.entry('Ime')
@record.entry('my_name()')
def my_name(name):
    return f'I am {name}'

@track.entry('Sve')
@record.entry('sve()')
@record.display(method='listed')
def sve():
    return

my_name('Noko')
sve()
'''
