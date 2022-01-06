# stores menu options over functions and class methods for listing.
class record:
    basic_menu = []
    descriptive_menu = []
    dictionary_menu = {}

    # initializes the object and function it is decorating.
    def __init__(self, func):
        self.func = func

    # creates and entry that is stored in a basic menu, descriptive menu and a dictionary menu.
    def entry(option_name, option_description = ''):

        def record_function(func):
            record.dictionary_menu[option_name] = func
            record.basic_menu += [option_name]
            descriptive_function = str(option_name) + ' - ' + str(option_description)
            record.descriptive_menu += [descriptive_function]

            def _wrap(*args, **kwargs):
                return func(*args, **kwargs)

            return _wrap
        return record_function

    # style ('decorator' - appends to a function.)
    # style ('function' - executes as a standalone function.)
    # method ('basic' - shows just record.entry stored names.)
    # method ('descriptive' - shows record.entry stored names and record.entry.option_description as a help menu.)
    # method ('dictionary' - creates a dictionary of record.entry names and the function they are appended on.)
    # return_option ('logs' - executes the function, but returns logs.)
    # return_option ('function' - shows logs, but returns the function.)
    def display(style = 'decorator', method = 'dictionary', return_option = 'logs'):
        if style == 'decorator':
            if return_option == 'logs':
                if method == 'basic':
                    def wrapper(func):
                        def decorator(*args, **kwargs):
                            func(*args,**kwargs)
                            return record.basic_menu
                        return decorator
                    return wrapper
                elif method == 'descriptive':
                    def wrapper(func):
                        def decorator(*args, **kwargs):
                            func(*args,**kwargs)
                            return record.descriptive_menu
                        return decorator
                    return wrapper
                elif method == 'dictionary':
                    def wrapper(func):
                        def decorator(*args, **kwargs):
                            func(*args,**kwargs)
                            return record.dictionary_menu
                        return decorator
                    return wrapper

            elif return_option == 'function':
                if method == 'basic':
                    def wrapper(func):
                        def decorator(*args, **kwargs):
                            print(record.basic_menu)
                            return func(*args,**kwargs)
                        return decorator
                    return wrapper
                elif method == 'descriptive':
                    def wrapper(func):
                        def decorator(*args, **kwargs):
                            print(record.descriptive_menu)
                            return func(*args,**kwargs)
                        return decorator
                    return wrapper
                elif method == 'dictionary':
                    def wrapper(func):
                        def decorator(*args, **kwargs):
                            print(record.dictionary_menu)
                            return func(*args,**kwargs)
                        return decorator
                    return wrapper
                
        elif style == 'function':
            if method == 'basic':
                return record.basic_menu
            elif method == 'descriptive':
                return record.descriptive_menu
            elif method == 'dictionary':
                return record.dictionary_menu

            
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
                    data =  {
                            'FUNCTION NAME: ' : func_name,
                            'EXECUTION TIME: ' : str(end - start),
                            'EXECUTED AT: ' : str(datetime.datetime.now()),
                            'MEMORY SIZE: ' : str(sys.getsizeof(func)) + ' bytes',
                            },

                    with open('Logs.json', 'a') as f:
                        f.write(json.dumps(data, indent = 4))
                        return results
                return logsaver
        return log

    # style ('decorator' - appends to a function.)
    # style ('function' - executes as a standalone function.)
    # return_option ('logs' - executes the function, but returns logs.)
    # return_option ('function' - shows logs, but returns the function - THIS DOES NOT RETURN THE LAST ENTRY FROM LOGS!!!)
    def display(style = 'decorator', return_option = 'logs'):
        if style == 'function':
            f = open('Logs.json', 'r')
            print(f.read())

        elif style == 'decorator':
            if return_option == 'logs':
                def wrapper(func):
                    def decorator(*args, **kwargs):
                        f = open('Logs.json', 'r')
                        func(*args, **kwargs)
                        logs = print(f.read())
                        return logs
                    return decorator
                return wrapper

            elif return_option == 'function':
                def wrapper(func):
                    def decorator(*args, **kwargs):
                        f = open('Logs.json', 'r')
                        print(f.read())
                        return func(*args, **kwargs)
                    return decorator
                return wrapper
