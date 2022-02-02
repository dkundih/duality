# makes multiple instances of the object available.
from duality.decorators.metaclass import Meta

# stores menu options over functions and class methods for listing.
class record(metaclass = Meta):

    # initializes the object and function it is decorating.
    def __init__(self,):
        self.basic_menu = []
        self.descriptive_menu = []
        self.dictionary_menu = {}

    # option_name - stores the name for the config and display functions.
    # option_description - stores the description of the function for the config and display functions.
    # -
    # creates and entry that is stored in a basic menu, descriptive menu and a dictionary menu.
    # DEFAULT: record.entry(option_name, option_description = '').
    def entry(self, option_name = '', option_description = ''):
        self.option_name = option_name
        self.option_description = option_description

        def record_function(func):
            self.dictionary_menu[self.option_name] = func
            self.basic_menu += [self.option_name]
            self.descriptive_function = str(self.option_name) + ' - ' + str(self.option_description)
            self.descriptive_menu += [self.descriptive_function]

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
    def display(self, style = 'decorator', method = 'dictionary', return_option = 'logs'):
        if style == 'decorator':
            if return_option == 'logs':
                if method == 'basic':
                    def wrapper(func):
                        def decorator(self,*args, **kwargs):
                            func(*args,**kwargs)
                            return self.basic_menu
                        return decorator
                    return wrapper
                elif method == 'descriptive':
                    def wrapper(func):
                        def decorator(self,*args, **kwargs):
                            func(*args,**kwargs)
                            return self.descriptive_menu
                        return decorator
                    return wrapper
                elif method == 'dictionary':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            func(*args,**kwargs)
                            return self.dictionary_menu
                        return decorator
                    return wrapper

            elif return_option == 'function':
                if method == 'basic':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            print(self.basic_menu)
                            return func(*args,**kwargs)
                        return decorator
                    return wrapper
                elif method == 'descriptive':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            print(self.descriptive_menu)
                            return func(*args,**kwargs)
                        return decorator
                    return wrapper
                elif method == 'dictionary':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            print(self.dictionary_menu)
                            return func(*args,**kwargs)
                        return decorator
                    return wrapper
                
        elif style == 'function':
            if method == 'basic':
                return self.basic_menu
            elif method == 'descriptive':
                return self.descriptive_menu
            elif method == 'dictionary':
                return self.dictionary_menu

    # display_headline - displays the desired headline.
    # display_message - displays input value message.
    # output_message - confirmation of the chosen value.
    # method ('descriptive' - shows stored option_name and it's description.)
    # method ('basic' - shows only the stored option_name.)
    # alignment ('basic' - shows all stored option_name and option_description values in a row.)
    # alignment ('newline' -shows all stored option_name and option_description values in a new line.)
    # -
    # creates an executeable menu from defined entries on top of functions.
    # DEFAULT: record.config(display_message = 'ENTER THE OPTION: ', output_message = 'YOU HAVE CHOSEN: ', method = 'descriptive', alignment = 'newline').
    def config(self, display_headline ='AVAILABLE OPTIONS', display_message = 'ENTER THE OPTION: ', output_message = 'YOU HAVE CHOSEN: ', method = 'descriptive', alignment = 'newline'):
        self.display_headline = display_headline
        self.display_message = display_message
        self.output_message = output_message
        if alignment == 'basic':
            if method == 'basic':
                show_menu = self.display(style = 'function', method = 'basic')
                print(self.display_headline)
                print('-----------------')
                print(show_menu)
            elif method == 'descriptive':
                show_menu = self.display(style = 'function', method = 'descriptive')
                print(self.display_headline)
                print('-----------------')
                print(show_menu)
            else:
                print('INVALID METHOD CHOSEN, THE PROGRAM WILL CONTINUE WITHOUT DISPLAYED OPTIONS.\n')
        elif alignment == 'newline':
            if method == 'basic':
                show_menu = self.display(style = 'function', method = 'basic')
                print(self.display_headline)
                print('-----------------')
                for line in show_menu:
                    print(line)
            elif method == 'descriptive':
                show_menu = self.display(style = 'function', method = 'descriptive')
                print(self.display_headline)
                print('-----------------')
                for line in show_menu:
                    print(line)
            else:
                print('INVALID METHOD CHOSEN, THE PROGRAM WILL CONTINUE WITHOUT DISPLAYED OPTIONS.\n')
        self.option = input('\n' + self.display_message)
        print(self.output_message, self.option + '\n')
        try:
            return self.dictionary_menu[self.option](self)
        except:
            return self.dictionary_menu[self.option]()
