# stores menu options over functions and class methods for listing.
class record:
    basic_menu = []
    descriptive_menu = []
    dictionary_menu = {}

    # initializes the object and function it is decorating.
    def __init__(self, func):
        self.func = func

    # option_name - stores the name for the config and display functions.
    # option_description - stores the description of the function for the config and display functions.
    # -
    # creates and entry that is stored in a basic menu, descriptive menu and a dictionary menu.
    # DEFAULT: record.entry(option_name, option_description = '').
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
    # -
    # outputs saved menu as a function or decorator.
    # DEFAULT: record.display(style = 'decorator', method = 'dictionary', return_option = 'logs').
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

    # display_message - displays input value message.
    # output_message - confirmation of the chosen value.
    # method ('descriptive' - shows stored option_name and it's description.)
    # method ('basic' - shows only the stored option_name.)
    # alignment ('basic' - shows all stored option_name and option_description values in a row.)
    # alignment ('newline' -shows all stored option_name and option_description values in a new line.)
    # -
    # creates an executeable menu from defined entries on top of functions.
    # DEFAULT: record.config(display_message = 'ENTER THE OPTION: ', output_message = 'YOU HAVE CHOSEN: ', method = 'descriptive', alignment = 'newline').
    def config(display_message = 'ENTER THE OPTION: ', output_message = 'YOU HAVE CHOSEN: ', method = 'descriptive', alignment = 'newline'):
        dictionary_menu = record.display(style = 'function', method = 'dictionary')
        if alignment == 'basic':
            if method == 'basic':
                show_menu = record.display(style = 'function', method = 'basic')
                print('AVAILABLE OPTIONS')
                print('-----------------')
                print(show_menu)
            elif method == 'descriptive':
                show_menu = record.display(style = 'function', method = 'descriptive')
                print('AVAILABLE OPTIONS')
                print('-----------------')
                print(show_menu)
            else:
                print('INVALID METHOD CHOSEN, THE PROGRAM WILL CONTINUE WITHOUT DISPLAYED OPTIONS.\n')
        elif alignment == 'newline':
            if method == 'basic':
                show_menu = record.display(style = 'function', method = 'basic')
                print('AVAILABLE OPTIONS')
                print('-----------------')
                for line in show_menu:
                    print(line)
            elif method == 'descriptive':
                show_menu = record.display(style = 'function', method = 'descriptive')
                print('AVAILABLE OPTIONS')
                print('-----------------')
                for line in show_menu:
                    print(line)
            else:
                print('INVALID METHOD CHOSEN, THE PROGRAM WILL CONTINUE WITHOUT DISPLAYED OPTIONS.\n')
        option = input('\n' + display_message)
        print(output_message, option + '\n')
        dictionary_menu[option]()

            
# tracks function behaviuor and stores it into a JSON file.
class track:

    # func_name - stores a function name it assigns to a JSON related object afterwards.
    # -
    # appends to a function and tracks it's execution details.
    # DEFAULT: track.entry(func_name).
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
                        f.close()
                        return results
                return logsaver
        return log

    # style ('decorator' - appends to a function.)
    # style ('function' - executes as a standalone function.)
    # return_option ('logs' - executes the function, but returns logs.)
    # return_option ('function' - shows logs, but returns the function - THIS DOES NOT RETURN THE LAST ENTRY FROM LOGS!!!)
    # -
    # outputs the saved JSON file entries.
    # DEFAULT: track.display(style = 'decorator', return_option = 'logs').
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
