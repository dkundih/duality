# makes multiple instances of the object available.
from logistics.plugins.metaclass import Meta

# imports all data types.
from logistics.plugins.types import *

# package.
class DualityApp(metaclass = Meta):

    '''
    * stores menu options over functions and class methods for listing.
    '''

    def __init__(
        self,
        ) -> ReturnType:

        '''
        * initializes the object and function it is decorating.
        '''

        self.basic_menu : ListType = []
        self.descriptive_menu : ListType = []
        self.dictionary_menu : DictionaryType = {}
        self.individual_dict : DictionaryType = {}
        self.reset_dict : DictionaryType = {}
        self.poolsize : IntegerType = 0
        self.stored_keys : ListType = []
        self.print_val_dict : ListType = {}

        self.hidden_basic_menu : ListType = []
        self.hidden_descriptive_menu : ListType = []
        self.hidden_dictionary_menu : DictionaryType = {}
        self.contains_autoinit : BooleanType = False

    def entry(
        self, 
        option_name : StringType = '', 
        option_description : StringType = '',
        autoinit: BooleanType = False,
        print_val: BooleanType = False,
        ) -> StringDictionary:

        '''
        * creates and entry that is stored in a basic menu, descriptive menu and a dictionary menu.

        - option_name - stores the name for the config and display functions.
        - option_description - stores the description of the function for the config and display functions.
        - autoinit (True/False) - automatically initializes the function without storing into the dictionary menu.
        - print_val (True/False) - enables the print of function output.
        # DEFAULT: Record.entry(option_name : StringType = '', option_description : StringType = '', autoinit : BooleanType = False, print_val : BooleanType = False).
        '''

        self.option_name = option_name
        self.option_description = option_description
        self.dict_name = self.option_name
        self.print_val = print_val
        self.individual_dict[self.dict_name] = {}
        self.reset_dict[self.dict_name] = {}
        self.print_val_dict[self.option_name] = self.print_val

        def _record_function(func):

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

        return _record_function

    def display(
        self,
        style : StringType = 'decorator', 
        method : StringType = 'dictionary', 
        return_option : StringType = 'logs',
        ) -> StringDictionary:

        '''
        * outputs saved menu as a function or decorator.

        - style ('decorator' - appends to a function.)
        - style ('function' - executes as a standalone function.)
        - method ('basic' - shows just record.entry stored names.)
        - method ('descriptive' - shows record.entry stored names and record.entry.option_description as a help menu.)
        - method ('dictionary' - creates a dictionary of record.entry names and the function they are appended on.)
        - return_option ('logs' - executes the function, but returns logs.)
        - return_option ('function' - shows logs, but returns the function.)
        # DEFAULT: Record.display(style : StringType = 'decorator', method : StringType = 'dictionary', return_option : StringType = 'logs'.)
        '''

        if style == 'decorator':
            if return_option == 'logs':
                if method == 'basic':
                    def _wrapper(func):
                        def _decorator(self,*args, **kwargs):
                            func(*args, **kwargs)
                            return self.basic_menu
                        return _decorator
                        
                    return _wrapper

                elif method == 'descriptive':
                    def _wrapper(func):
                        def _decorator(self,*args, **kwargs):
                            func(*args, **kwargs)
                            return self.descriptive_menu
                        return _decorator

                    return _wrapper

                elif method == 'dictionary':
                    def _wrapper(func):
                        def _decorator(self, *args, **kwargs):
                            func(*args, **kwargs)
                            return self.dictionary_menu
                        return _decorator

                    return _wrapper

            elif return_option == 'function':
                if method == 'basic':
                    def _wrapper(func):
                        def _decorator(self, *args, **kwargs):
                            print(self.basic_menu)
                            return func(*args, **kwargs)
                        return _decorator

                    return _wrapper

                elif method == 'descriptive':
                    def _wrapper(func):
                        def _decorator(self, *args, **kwargs):
                            print(self.descriptive_menu)
                            return func(*args, **kwargs)
                        return _decorator

                    return _wrapper

                elif method == 'dictionary':
                    def _wrapper(func):
                        def _decorator(self, *args, **kwargs):
                            print(self.dictionary_menu)
                            return func(*args, **kwargs)
                        return _decorator

                    return _wrapper
                
        elif style == 'function':
            if method == 'basic':
                return self.basic_menu

            elif method == 'descriptive':
                return self.descriptive_menu

            elif method == 'dictionary':
                return self.dictionary_menu

    def config(
        self, 
        type : StringType = 'static', 
        display_headline : StringType ='AVAILABLE OPTIONS', 
        display_message : StringType = 'ENTER THE OPTION: ', 
        output_message : StringType = 'YOU HAVE CHOSEN: ',
        choice_message : StringType = 'CONTINUE? (Y/N): ',
        enter_message : StringType = 'ENTER THE: ',
        method : StringType = 'descriptive', 
        alignment : StringType = 'newline',
        queue: BooleanType = False,
        show_dtypes: BooleanType = True,
        ) -> SpecialType:

        '''
        * creates an executable menu from defined entries on top of functions.

        - type ('static' - adapts to the execution of static non-self methods and functions.)
        - type ('dynamic' - adapts to the execution of dynamic class self methods and functions.)
        - display_headline - displays the desired headline.
        - display_message - displays input value message.
        - output_message - confirmation of the chosen value.
        - choice_message - output choice message.
        - enter_message - enter choice message.
        - method ('descriptive' - shows stored option_name and it's description.)
        - method ('basic' - shows only the stored option_name.)
        - alignment ('basic' - shows all stored option_name and option_description values in a row.)
        - alignment ('newline' -shows all stored option_name and option_description values in a new line.)
        - queue (True/False) - enables stacking of functions and executing them in a chain.
        - show_dtypes (True/False) - shows the dtype of the input value.
        # DEFAULT: Record.config(type : StringType = 'static', display_headline : StringType = 'AVAILABLE OPTIONS', display_message : StringType = 'ENTER THE OPTION: ', output_message : StringType = 'YOU HAVE CHOSEN: ', choice_message : StringType = 'CONTINUE? (Y/N): ', enter_message : StringType = 'ENTER THE: ', method : StringType = 'descriptive', alignment : StringType = 'newline', queue : BooleanType = False, show_dtypes : BooleanType = True).
        '''

        self.display_headline = display_headline
        self.display_message = display_message
        self.output_message = output_message
        self.choice_message = choice_message
        self.enter_message = enter_message
        self.queue = queue
        self.show_dtypes = show_dtypes
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
            self.print_option = self.print_val_dict[self.option]
            print(self.output_message, self.option + '\n')

            # executes autoinit function.
            if self.contains_autoinit == True:

                try:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i](self)
                except:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i]()

            # disables a loop of functions.
            self._queue_break()

            if type == 'static':
                print(self.tmp_name_list[self.yield_name])

                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    print(self.tmp_name_list[self.yield_name])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(**self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(self, **self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1

            elif type == 'dynamic':
                
                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    print(self.tmp_name_list[self.yield_name])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(self, **self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(**self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1

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
            self._queue_handler()

            if type == 'static':
                print(self.tmp_name_list[self.yield_name])

                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    print(self.tmp_name_list[self.yield_name])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(self, **self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(**self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1

            elif type == 'dynamic':
                
                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    print(self.tmp_name_list[self.yield_name])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(**self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(self, **self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1

        return

    def store(
        self,
        variable : StringType = '',
        type : StringType = 'str',
        ) -> DictionaryType:

        '''
        * function that stores the input value in a dictionary.

        - variable - name of the function argument input is being passed as.
        - type - type of the data being passed ('int', 'float', 'str' and 'list' supported.)
        # DEFAULT: Record.store(variable : StringType = '', type : StringType = 'str'.)
        '''

        self.type = type
        self.variable = variable
        self.individual_dict[self.dict_name][self.variable] = self.type
        self.reset_dict[self.dict_name][self.variable] = self.type

        return self.dict_name

    # this is a help function, do not call it when using a package.
    def _redefine(
        self,
        ) -> DictionaryType:

        '''
        * function that casts an input of a certain data type and formats it before sending as a function argument.
        '''

        if self.show_dtypes == True:
            if self.reset_dict[self.clone_dict]:
                print(self.reset_dict[self.clone_dict])

        for i in self.individual_dict[self.clone_dict]:
            self.format = self.reset_dict[self.clone_dict][i]
            if self.format != 'list':
                self.new_i = input(self.enter_message + f'{i}: ')
            self.dtypes = {
            'int': self._set_int,
            'float': self._set_float,
            'str': self._set_str,
            'list' : self._set_list,
        }
            self.new_i = self.dtypes[self.format]()
            self.individual_dict[self.clone_dict][i] = self.new_i

        return self.individual_dict[self.clone_dict]

    # this is a help function, do not call it when using a package.
    def _set_int(
        self,
        ) -> ReturnType:

        '''
        * converts input to integer.
        '''

        self.new_i = int(self.new_i)
        return self.new_i

    # this is a help function, do not call it when using a package.
    def _set_float(
        self,
        ) -> ReturnType:
        
        '''
        * converts input to float.
        '''

        self.new_i = float(self.new_i)
        return self.new_i

    # this is a help function, do not call it when using a package.
    def _set_str(
        self,
        ) -> ReturnType:

        '''
        * converts input to string.
        '''

        self.new_i = str(self.new_i)
        return self.new_i

    # this is a help function, do not call it when using a package.
    def _set_list(
        self,
        ) -> ReturnType:
        
        '''
        * converts input to list.
        '''

        self.range = int(input('Number of list values: '))
        self.new_i = []

        for i in range(0, self.range):
            tmp_list_element = int(input(f'Enter the value: '))
            self.new_i.append(tmp_list_element)
            
        return self.new_i

    # this is a help function, do not call it when using a package.
    def _queue_handler(
        self,
        iterate: BooleanType = True,
        ) -> ListType:

        '''
        * enables a loop for the queue.

        - iterate (True/False) - enables the functionality of queue, do not change!
        '''

        self.print_val_list = []
        self.tmp_list = []
        self.iterate = iterate
        self.tmp_name_list = []
        self.tmp_print_list = []

        while self.iterate == True:
            self.option = input('\n' + self.display_message)
            self.tmp_name_list += [self.option]
            self.print_val_list += self.option
            print(self.output_message, self.option + '\n')
            self.tmp_list += [self.dictionary_menu[self.option]]
            self.tmp_print_list += [self.print_val_dict[self.option]]
            choice = input(self.choice_message)
            choice = choice.upper()

            if choice != 'Y':
                self.iterate = False
                print('')
        
        return self.tmp_list

    # this is a help function, do not call it when using a package.
    def _queue_break(
        self,
        ) -> ListType:

        '''
        * breaks the loop for the queue.
        '''

        self.print_val_list = []
        self.tmp_list = []
        self.tmp_name_list = []
        self.tmp_print_list = []

        self.tmp_name_list += [self.option]
        self.print_val_list += self.option
        print(self.output_message, self.option + '\n')
        self.tmp_list += [self.dictionary_menu[self.option]]
        self.tmp_print_list += [self.print_val_dict[self.option]]

        return self.tmp_list
