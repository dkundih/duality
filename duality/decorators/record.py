# makes multiple instances of the object available.
from vandal.plugins.metaclass import Meta

# imports custom types.
from vandal.plugins.types import (
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
    AnyType,
)


# stores menu options over functions and class methods for listing.
class Record(metaclass = Meta):

    # initializes the object and function it is decorating.
    def __init__(
        self,
        ) -> ReturnType:

        self.basic_menu : ListType = []
        self.descriptive_menu : ListType = []
        self.dictionary_menu : DictionaryType = {}

        self.hidden_basic_menu : ListType = []
        self.hidden_descriptive_menu : ListType = []
        self.hidden_dictionary_menu : DictionaryType = {}
        self.contains_autoinit : BooleanType = False


    # option_name - stores the name for the config and display functions.
    # option_description - stores the description of the function for the config and display functions.
    # autoinit (True/False) - automatically initializes the function without storing into the dictionary menu.
    # -
    # creates and entry that is stored in a basic menu, descriptive menu and a dictionary menu.
    # DEFAULT: record.entry(option_name, option_description = '', autoinit = False).
    def entry(
        self, 
        option_name : StringType = '', 
        option_description : StringType = '',
        autoinit: BooleanType = False,
        ) -> StringDictionary:

        self.option_name = option_name
        self.option_description = option_description

        def record_function(func):

            if autoinit == False:
                self.dictionary_menu[self.option_name] = func
                self.basic_menu += [self.option_name]
                self.descriptive_function = str(self.option_name) + ' - ' + str(self.option_description)
                self.descriptive_menu += [self.descriptive_function]
            
            elif autoinit == True:
                self.hidden_dictionary_menu[self.option_name] = func
                self.hidden_basic_menu += [self.option_name]
                self.descriptive_function = str(self.option_name) + ' - ' + str(self.option_description)
                self.hidden_descriptive_menu += [self.descriptive_function]
                self.contains_autoinit = True

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
    def display(
        self,
        style : StringType = 'decorator', 
        method : StringType = 'dictionary', 
        return_option : StringType = 'logs',
        ) -> StringDictionary:

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


    # type ('static' - adapts to the execution of static non-self methods and functions.)
    # type ('dynamic' - adapts to the execution of dynamic class self methods and functions.)
    # display_headline - displays the desired headline.
    # display_message - displays input value message.
    # output_message - confirmation of the chosen value.
    # method ('descriptive' - shows stored option_name and it's description.)
    # method ('basic' - shows only the stored option_name.)
    # alignment ('basic' - shows all stored option_name and option_description values in a row.)
    # alignment ('newline' -shows all stored option_name and option_description values in a new line.)
    # queue (True/False) - enables stacking of functions and executing them in a chain.
    # -
    # creates an executeable menu from defined entries on top of functions.
    # DEFAULT: record.config(type = 'static', display_headline ='AVAILABLE OPTIONS', display_message = 'ENTER THE OPTION: ', output_message = 'YOU HAVE CHOSEN: ', method = 'descriptive', alignment = 'newline', queue = False).
    def config(
        self, 
        type : StringType = 'static', 
        display_headline : StringType ='AVAILABLE OPTIONS', 
        display_message : StringType = 'ENTER THE OPTION: ', 
        output_message : StringType = 'YOU HAVE CHOSEN: ', 
        method : StringType = 'descriptive', 
        alignment : StringType = 'newline',
        queue: BooleanType = False,
        ) -> DictionaryType:

        self.display_headline = display_headline
        self.display_message = display_message
        self.output_message = output_message
        self.queue = queue
        self.yield_name = 0 # list item counter that enables iterating through the list.

        # assert type.
        if type != 'static' and type != 'dynamic':
            type = 'static'
            print('WARNING: Automactically forced type to static due to invalid type choice.')
            print('Write type = \'static\' or type = \'dynamic\' in the config option to change how this impacts the behaviour of executed functions in the menu.')
            print('')

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

        if queue == False:

            self.option = input('\n' + self.display_message)

            print(self.output_message, self.option + '\n')

            # executes autoinit function.
            if self.contains_autoinit == True:

                try:

                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i](self)
                except:
                    
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i]()

            if type == 'static':

                try:
                    return self.dictionary_menu[self.option](self)

                except:
                    return self.dictionary_menu[self.option]()

            elif type == 'dynamic':

                try:
                    return self.dictionary_menu[self.option]()
                except:
                    return self.dictionary_menu[self.option](self)

        if queue == True:
            # executes autoinit functions.
            if self.contains_autoinit == True:

                try:

                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i](self)
                except:
                    
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i]()

            # enables a loop to execute functions in a chain.
            self.queue_handler()

            if type == 'static':

                print(self.tmp_name_list[self.yield_name])

                for tmp_func in self.tmp_list:

                    try:
                        tmp_func(self)
                        print('')
                        self.yield_name += 1
                    except:
                        tmp_func()
                        print('')
                        self.yield_name += 1

            elif type == 'dynamic':

                for tmp_func in self.tmp_list:

                    print(self.tmp_name_list[self.yield_name])

                    try:
                        tmp_func()
                        print('')
                        self.yield_name += 1
                    except:
                        tmp_func(self)
                        print('')
                        self.yield_name += 1

        return

    # iterate (True/False) - enables the functionality of queue, do not change!
    # -
    # enables a loop for the queue.
    def queue_handler(
        self,
        iterate: BooleanType = True,
        ) -> ReturnType:

        self.tmp_list = []
        self.iterate = iterate
        self.tmp_name_list = []
        
        while self.iterate == True:

            self.option = input('\n' + self.display_message)

            self.tmp_name_list += [self.option]

            print(self.output_message, self.option + '\n')

            self.tmp_list += [self.dictionary_menu[self.option]]

            choice = input('Continue? (Y/N): ')

            choice = choice.upper()

            if choice != 'Y':

                self.iterate = False
                print('')
        
        return self.tmp_list


    # input_val - input value to be used in the function.
    # dtype - data type of the input value.
    # -
    # enables the user to input a value and store it in a variable within a decorated function.
    def define(
        self,
        input_val: StringType = '',
        dtype: AnyType = 'str',
      ) -> DictionaryType:

        self.inputs = input_val
        self.input_dict = {}
        key = input_val
        value = input(f'Enter the {input_val}: ')
        # available data types
        dtypes = {
            'int': int(value),
            'float': float(value),
            'str': str(value),
            'bool': bool(value),
            'list': list(value),
            'tuple': tuple(value),
            'dict': {'value' : value},
            'vector': [value],
          }

        value = dtypes[dtype]
        self.input_dict[key] = value
        return self.input_dict[key]
