# makes multiple instances of the object available.
from logistics.plugins.metaclass import Meta

# set type of numpy array and pandas particles.
import numpy as np
import pandas as pd

# for CLI functionality.
import os
from colorama import (
    Fore,
    Back,
    Style,
    init,
)

init()

# imports all data types.
from logistics.plugins.types import *

# imports coloring.
from logistics.plugins.coloring import *


# main object.
class DualityApp(metaclass = Meta):

    '''
    * stores menu options over functions and class methods for listing.
    
    COLORSET (custom_color_mode template)
    ________
    
    colorset = {
        'credit' : 'Fy', - credit pop-up color.
        'display_headline' : 'Fy', - headline of the menu color.
        'display_message' : 'Fc', - enter the option color.
        'output_message' : 'Fy', - confirmation of choice color (DEPRECATED).
        'enter_message' : 'Fc', - input variables color.
        'tmp_name_list' : 'Fy', - headline of chosen option color.
        'tmp_func' : 'Fc', - output of the chosen option color.
        'warning' : 'Fr', - general warning and error handling color.
        'exit_message' : 'Fy', - exit out of the application color.
    }
    '''

    def __init__(
        self,
        credit : StringType = 'duality © David Kundih, 2021 -',
        include : ListType = ['menu', 'cls', 'exit'],
        ) -> ReturnType:

        '''
        * initializes the object and function it is decorating.
        
        credit - headline credit of the application.
        include - includes pre-built options for menu, clear screen and exit.
        
        # DEFAULT: DualityApp(credit : StringType = 'duality © David Kundih, 2021 -', include : ListType = ['menu', 'cls', 'exit'])
        '''
        
        self.credit : StringType = credit
        self.include : ListType = include
        self.basic_menu : ListType = []
        self.descriptive_menu : ListType = []
        self.dictionary_menu : DictionaryType = {}
        self.individual_dict : DictionaryType = {}
        self.reset_dict : DictionaryType = {}
        self.poolsize : IntegerType = 0
        self.stored_keys : ListType = []
        self.print_val_dict : ListType = {}
        self.option_names : ListType = []
        self.overwrite_variable : DictionaryType = {}
        self.overwrite_types : DictionaryType = {}
        self.verbose_display_message_list : ListType = []
        self.verbose_set : ReturnType = None # prevents duplicate verbose option list creation.

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

        - option_name - stores the name for the display of functions.
        - option_description - stores the description of the function for display functions.
        - autoinit (True/False) - automatically initializes the function without storing into the dictionary menu.
        - print_val (True/False) - enables the print of function output.
        # DEFAULT: DualityApp.entry(option_name : StringType = '', option_description : StringType = '', autoinit : BooleanType = False, print_val : BooleanType = False).
        '''

        self.option_name = option_name
        self.option_names += [self.option_name]
        self.option_description = option_description
        self.dict_name = self.option_name
        self.verbose_display_message_list += [self.option_name]
        self.print_val = print_val
        self.individual_dict[self.dict_name] = {}
        self.reset_dict[self.dict_name] = {}
        self.overwrite_variable[self.dict_name] = {} # store redefine.
        self.overwrite_types[self.dict_name] = {} # store redefine.
        self.print_val_dict[self.option_name] = self.print_val

        def _record_function(func):

            if autoinit == False:
                self.dictionary_menu[self.option_name] = func
                self.basic_menu += [self.option_name]
                self.descriptive_function = str(self.option_name) + str(paint_text(' -> ', color = 'Fy', print_trigger = False)) + str(self.option_description)
                self.descriptive_menu += [self.descriptive_function]
            
            elif autoinit == True:
                self.hidden_dictionary_menu[self.option_name] = func
                self.hidden_basic_menu += [self.option_name]
                self.descriptive_function = str(self.option_name) + str(paint_text(' -> ', color = 'Fy', print_trigger = False)) + str(self.option_description)
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
        - method ('basic' - shows just DualityApp.entry stored names.)
        - method ('descriptive' - shows DualityApp.entry stored names and DualityApp.entry.option_description as a help menu.)
        - method ('dictionary' - creates a dictionary of DualityApp.entry names and the function they are appended on.)
        - return_option ('logs' - executes the function, but returns logs.)
        - return_option ('function' - shows logs, but returns the function.)
        # DEFAULT: DualityApp.display(style : StringType = 'decorator', method : StringType = 'dictionary', return_option : StringType = 'logs'.)
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


    def script(
        self, 
        type : StringType = 'dynamic', 
        display_headline : StringType ='AVAILABLE OPTIONS',
        verbose_display_message : BooleanType = True,
        display_message : StringType = 'ENTER THE OPTION ',
        output_message : StringType = 'YOU HAVE CHOSEN: ',
        break_key : StringType = 'exit',
        exit_message : StringType = 'Exiting...',
        enter_message : StringType = 'ENTER THE ',
        method : StringType = 'descriptive', 
        alignment : StringType = 'newline',
        queue: StringType = 'y',
        show_dtypes: BooleanType = True,
        show_confirmation : BooleanType = False,
        color_mode : StringType = 'dark',
        custom_color_mode : DictionaryType = None,
        clear_screen : BooleanType = True,
        ) -> SpecialType:

        '''
        * creates an executable menu from defined entries on top of functions.

        - type ('static' - adapts to the execution of static non-self methods and functions.)
        - type ('dynamic' - adapts to the execution of an object class self methods and functions as dynamic.)
        - display_headline - displays the desired headline.
        - verbose_display_message (True/False) - displays all menu options next to the input option request.
        - display_message - displays input value message.
        - output_message - confirmation of the chosen value.
        - break_key - key that breaks the loop while queue = 'y'.
        - exit_message - message while exiting.
        - enter_message - enter choice message.
        - method ('descriptive' - shows stored option_name and it's description.)
        - method ('basic' - shows only the stored option_name.)
        - alignment ('basic' - shows all stored option_name and option_description values in a row.)
        - alignment ('newline' -shows all stored option_name and option_description values in a new line.)
        - queue (DO NOT CHANGE!) - enables stacking of functions and executing them in a chain.
        - show_dtypes (True/False) - shows the dtype of the input value.
        - show_confirmation (True/False) - confirmation of the chosen option.
        - color_mode ('dark' - for dark terminal.)
        - color_mode ('light' - for light terminal.)
        - custom_color_mode - custom dictionary set of colors.
        - clear_screen (True/False) - clears the screen before starting the app
        
        # DEFAULT: DualityApp.script(
        type : StringType = 'dynamic', 
        display_headline : StringType ='AVAILABLE OPTIONS',
        verbose_display_message : BooleanType = True,
        display_message : StringType = 'ENTER THE OPTION ', 
        output_message : StringType = 'YOU HAVE CHOSEN: ',
        break_key : StringType = 'exit',
        exit_message : StringType = 'Exiting...',
        enter_message : StringType = 'ENTER THE ',
        method : StringType = 'descriptive', 
        alignment : StringType = 'newline',
        queue: StringType = 'y',
        show_dtypes: BooleanType = True,
        show_confirmation : BooleanType = False,
        color_mode : StringType = 'dark',
        custom_color_mode : DictionaryType = None,
        clear_screen : BooleanType = True
        ) -> SpecialType:
        '''

        self.clear_screen = clear_screen

        if self.clear_screen == True:
            os.system('cls')

        self.color_mode = color_mode # dark or ligth appearance.
        self.custom_color_mode = custom_color_mode # option to introduce own color dictionary.

        # set up coloring in the CLI.
        if self.color_mode == 'dark':
            self.colorset = {
                'credit' : 'Fy',
                'display_headline' : 'Fy',
                'display_message' : 'Fc',
                'output_message' : 'Fy',
                'enter_message' : 'Fc',
                'tmp_name_list' : 'Fy',
                'tmp_func' : 'Fc',
                'warning' : 'Fr',
                'exit_message' : 'Fy',
            }
        
        elif self.color_mode == 'light':
            self.colorset = {
                'credit' : 'Fg',
                'display_headline' : 'Fg',
                'display_message' : 'Fb',
                'output_message' : 'Fg',
                'enter_message' : 'Fb',
                'tmp_name_list' : 'Fg',
                'tmp_func' : 'Fb',
                'warning' : 'Fr',
                'exit_message' : 'Fg',
            }
        
        elif self.color_mode == 'custom':
            self.colorset = self.custom_color_mode
        
        self.break_key = break_key

        self.display_headline = display_headline
        self.verbose_display_message = verbose_display_message # displays all menu options next to the input option request.
        
        if 'menu' in self.include:
            if 'menu' not in self.option_names:
                @self.entry('menu', 'shows the menu.')
                def _show_menu(self):
                    paint_text(self.credit, self.colorset['credit'], print_trigger = True)
                    print('')
                    show_menu = self.display(style = 'function', method = 'descriptive')
                    paint_text(self.display_headline, self.colorset['display_headline'])
                    print('-----------------')
                    for line in show_menu:
                        print(line)
                    if 'exit' in self.include:
                        print(str(self.break_key) + str(paint_text(' -> ', color = 'Fr', print_trigger = False)) + 'exit.')
            
        if 'cls' in self.include:
            if 'cls' not in self.option_names:
                @self.entry('cls', 'clears the screen.')
                def _clear_screen(self):
                    os.system('cls')
                    paint_text(self.credit, self.colorset['credit'], print_trigger = True)
                    print('')
                    show_menu = self.display(style = 'function', method = 'descriptive')
                    paint_text(self.display_headline, self.colorset['display_headline'])
                    print('-----------------')
                    for line in show_menu:
                        print(line)
                    if 'exit' in self.include:
                        print(str(self.break_key) + str(paint_text(' -> ', color = 'Fr', print_trigger = False)) + 'exit.')
                        
        if self.break_key not in self.verbose_display_message_list:
            self.verbose_display_message_list.append(self.break_key)
            
        if self.verbose_set != True:
            if self.verbose_display_message == True:
                self.verbose_set = True
                self.display_message = paint_text(display_message + str(self.verbose_display_message_list) + ': ', self.colorset['display_message'], print_trigger = False)
            elif self.verbose_display_message == False:
                self.display_message = paint_text(display_message, self.colorset['display_message'], print_trigger = False)
        else:
            self.display_message = paint_text(display_message, self.colorset['display_message'], print_trigger = False)
        
        self.output_message = paint_text(output_message, self.colorset['output_message'], print_trigger = False)
        self.enter_message = paint_text(enter_message, self.colorset['enter_message'], print_trigger = False)
        self.queue = queue
        self.show_dtypes = show_dtypes
        self.yield_name = 0 # list item counter that enables iterating through the list.
        self.show_confirmation = show_confirmation # confirmation of chosen option.
        self.exit_message = exit_message # message while exiting.
        
        # assert deprecated warning.
        if self.queue == 'n':
            print('WARNING: Option is deprecated.')
            print('Write type = \'script\' or type = \'wheel\' to change how this impacts the behaviour of executed functions in the menu.')
            print('')

        if alignment == 'basic':

            if method == 'basic':
                paint_text(self.credit, self.colorset['credit'], print_trigger = True)
                print('')
                show_menu = self.display(style = 'function', method = 'basic')
                paint_text(self.display_headline, self.colorset['display_headline'])
                print('-----------------')
                print(show_menu)
                if 'exit' in self.include:
                    print(str(self.break_key) + str(paint_text(' -> ', color = 'Fr', print_trigger = False)) + 'exit.')
                print('')

            elif method == 'descriptive':
                paint_text(self.credit, self.colorset['credit'], print_trigger = True)
                print('')
                show_menu = self.display(style = 'function', method = 'descriptive')
                paint_text(self.display_headline, self.colorset['display_headline'])
                print('-----------------')
                print(show_menu)
                if 'exit' in self.include:
                    print(str(self.break_key) + str(paint_text(' -> ', color = 'Fr', print_trigger = False)) + 'exit.')
                print('')

            elif method == 'none':
                pass

        elif alignment == 'newline':

            if method == 'basic':
                paint_text(self.credit, self.colorset['credit'], print_trigger = True)
                print('')
                show_menu = self.display(style = 'function', method = 'basic')
                paint_text(self.display_headline, self.colorset['display_headline'])
                print('-----------------')
                for line in show_menu:
                    print(line)
                if 'exit' in self.include:
                    print(str(self.break_key) + str(paint_text(' -> ', color = 'Fr', print_trigger = False)) + 'exit.')
                print('')
                
            elif method == 'descriptive':
                paint_text(self.credit, self.colorset['credit'], print_trigger = True)
                print('')
                show_menu = self.display(style = 'function', method = 'descriptive')
                paint_text(self.display_headline, self.colorset['display_headline'])
                print('-----------------')
                for line in show_menu:
                    print(line)
                if 'exit' in self.include:
                    print(str(self.break_key) + str(paint_text(' -> ', color = 'Fr', print_trigger = False)) + 'exit.')
                print('')
                
            elif method == 'none':
                pass

        if queue == 'n':

            self.option = input(self.display_message)
            self.print_option = self.print_val_dict[self.option]
            
            if self.output_message == True:
                print(self.output_message, self.option)

            print('')
            
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
                                
        # THIS OPTION IS ONLY FOR INTERNAL USE, DO NOT ATTEMPT TO USE IT OUTSIDE OF THE SCRIPT OR WHEEL METHODS.
        if queue == 'y':
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

                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    paint_text(self.tmp_name_list[self.yield_name], self.colorset['tmp_name_list'])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(self, **self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(**self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1
                              
                paint_text(self.exit_message, self.colorset['exit_message'], print_trigger = True)

            elif type == 'dynamic':
                
                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    paint_text(self.tmp_name_list[self.yield_name], self.colorset['tmp_name_list'])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(**self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(self, **self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1
                            
                paint_text(self.exit_message, self.colorset['exit_message'], print_trigger = True)
        
        if queue == 'wheel' or queue == 'w':
            
            # executes autoinit functions.
            if self.contains_autoinit == True:
                try:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i](self)
                except:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i]()

            # enables a loop to execute functions in a wheel loop.
            self._wheel_queue_handler()
                                
            if type == 'dynamic':

                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    paint_text(self.tmp_name_list[self.yield_name], self.colorset['tmp_name_list'])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(self, **self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(**self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1
                            
            if type == 'static':

                for tmp_func in self.tmp_list:
                    self.clone_dict = self.tmp_name_list[self.yield_name]
                    self.print_option = self.tmp_print_list[self.yield_name]
                    paint_text(self.tmp_name_list[self.yield_name], self.colorset['tmp_name_list'])

                    self._redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(self, **self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            paint_text(tmp_func(**self.individual_dict[self.clone_dict]), self.colorset['tmp_func'])
                            print('')
                            self.yield_name += 1

        return
    
    
    # wheel application.
    def wheel(
        self,
        type = 'dynamic',
        display_headline : StringType ='AVAILABLE OPTIONS',
        verbose_display_message : BooleanType = True,
        display_message : StringType = 'ENTER THE OPTION ',
        output_message : StringType = 'YOU HAVE CHOSEN: ',
        enter_message : StringType = 'ENTER THE ',
        color_mode : StringType = 'dark',
        custom_color_mode : DictionaryType = None,
        clear_screen = True,
        break_key = 'exit',
        exit_message = 'Exiting...'
        ) -> SpecialType:
        
        '''
        Limited changing capabilities, for more information about method variables examine script method.
        
        # DEFAULT: DualityApp.wheel(
        type = 'dynamic',
        display_headline : StringType ='AVAILABLE OPTIONS',
        verbose_display_message : BooleanType = True,
        display_message : StringType = 'ENTER THE OPTION ',
        output_message : StringType = 'YOU HAVE CHOSEN: ',
        enter_message : StringType = 'ENTER THE ',
        color_mode : StringType = 'dark',
        custom_color_mode : DictionaryType = None,
        clear_screen = True,
        break_key = 'exit',
        exit_message = 'Exiting...'
        ) -> SpecialType:
        '''
        
        self.clear_screen = clear_screen
        self.display_headline = display_headline
        self.type = type

        if self.clear_screen == True:
            os.system('cls')
            
        self.color_mode = color_mode # dark or ligth appearance.
        self.custom_color_mode = custom_color_mode # option to introduce own color dictionary.
        
        # set up coloring in the CLI.
        if self.color_mode == 'dark':
            self.colorset = {
                'credit' : 'Fy',
                'display_headline' : 'Fy',
                'display_message' : 'Fc',
                'output_message' : 'Fy',
                'enter_message' : 'Fc',
                'tmp_name_list' : 'Fy',
                'tmp_func' : 'Fc',
                'warning' : 'Fr',
                'exit_message' : 'Fy',
            }
        
        elif self.color_mode == 'light':
            self.colorset = {
                'credit' : 'Fg',
                'display_headline' : 'Fg',
                'display_message' : 'Fb',
                'output_message' : 'Fg',
                'enter_message' : 'Fb',
                'tmp_name_list' : 'Fg',
                'tmp_func' : 'Fb',
                'warning' : 'Fr',
                'exit_message' : 'Fg',
            }
        
        elif self.color_mode == 'custom':
            self.colorset = self.custom_color_mode
            
        self.display_message = display_message # basic display message.
        self.verbose_display_message = verbose_display_message # displays all menu options next to the input option request.
    
        self.output_message = output_message
        self.enter_message = enter_message
        self.break_key = break_key
        self.exit_message = exit_message
        
        paint_text(self.credit, self.colorset['credit'], print_trigger = True)
        print('')
        show_menu = self.display(style = 'function', method = 'descriptive')
        paint_text(self.display_headline, self.colorset['display_headline'])
        print('-----------------')
        for line in show_menu:
            print(line)
        if 'menu' in self.include:
            print('menu' + str(paint_text(' -> ', color = 'Fy', print_trigger = False)) + 'shows the menu.')
        if 'cls' in self.include:
            print('cls' + str(paint_text(' -> ', color = 'Fy', print_trigger = False)) + 'clears the screen.')
        if 'exit' in self.include:
            print(str(self.break_key) + str(paint_text(' -> ', color = 'Fr', print_trigger = False)) + 'exit.')
        print('')
        
        while True:
            if self.type == 'dynamic':
                self.script(type = 'dynamic', queue = 'wheel', method = 'none', clear_screen = False, verbose_display_message = self.verbose_display_message, display_message = self.display_message, output_message = self.output_message, color_mode = self.color_mode, custom_color_mode = self.custom_color_mode, break_key = self.break_key, enter_message = self.enter_message, exit_message = self.exit_message)
            if self.type == 'static':
                self.script(type = 'static', queue = 'wheel', method = 'none', clear_screen = False, verbose_display_message = self.verbose_display_message, display_message = self.display_message, output_message = self.output_message, color_mode = self.color_mode, custom_color_mode = self.custom_color_mode, break_key = self.break_key, enter_message = self.enter_message, exit_message = self.exit_message)
 
 
    def store(
        self,
        variable : StringType = '',
        type : StringType = 'str',
        overwrite : StringType = None,
        ) -> DictionaryType:

        '''
        * function that stores the input value in a dictionary.

        - variable - name of the function argument input is being passed as.
        - type - type of the data being passed ('int', 'float', 'str' and 'list' supported.)
        - overwrite - custom text that overwrites the variable name when shown in the CLI.
        # DEFAULT: DualityApp.store(variable : StringType = '', type : StringType = 'str', overwrite : StringType = None.)
        '''

        if overwrite == None:
            overwrite = variable

        self.type = type
        self.variable = variable
        self.overwrite = overwrite
        self.individual_dict[self.dict_name][self.variable] = self.type
        self.reset_dict[self.dict_name][self.variable] = self.type
        self.overwrite_variable[self.dict_name][self.variable] = self.overwrite
        self.overwrite_types[self.dict_name][self.overwrite] = self.type
        
        return self.dict_name


    # this is a help function, do not call it when using a package.
    def _redefine(
        self,
        ) -> DictionaryType:

        '''
        * function that casts an input of a certain data type and formats it before sending as a function argument.
        '''

        self._ignore_list = ['list', 'numlist', 'strlist', 'np.1darray', 'np.2darray', 'pd.df', 'pd.columns', 'path'] # ignores initial input and replaces it with a loop type/special type input.
        
        if self.show_dtypes == True:
            if self.overwrite_types[self.clone_dict]:
                print(self.overwrite_types[self.clone_dict])
                
            elif self.reset_dict[self.clone_dict]:
                print(self.reset_dict[self.clone_dict])

        for i in self.individual_dict[self.clone_dict]:
            self.tmp_msg = self.overwrite_variable[self.clone_dict][i]
            self.format = self.reset_dict[self.clone_dict][i]
            
            if self.format not in self._ignore_list:
                self.new_i = input(self.enter_message + paint_text(f'{self.tmp_msg}: ', color = self.colorset['enter_message'], print_trigger = False)) # initial input before transformation.
            self.dtypes = {
            'int': self._set_int, # -> single integer value.
            'float': self._set_float, # -> single float value.
            'str': self._set_str, # -> single text value.
            'list' : self._set_list, # -> list that supports both textual and numerical inputs.
            'numlist' : self._set_num_list, # -> list that supports numerical inputs only.
            'strlist' : self._set_str_list, # -> list that supports textual inputs only.
            'np.1darray' : self._set_numpy_1darray, # -> list that supports numerical inputs only and transforms it into a numpy array of 1 dimension.
            'np.2darray' : self._set_numpy_2darray, # -> list that supports numerical inputs only and transforms it into a numpy array of 2 dimensions.
            'pd.df' : self._set_pandas_df, # -> creates a pandas dataframe from a whole file path file (.csv, .xlsx, .json).
            'pd.columns' : self._set_pandas_columns, # -> creates a pandas dataframe from a file path file with certain column/s only (.csv, .xlsx, .json).
            'path' : self._set_path, # -> stores the file path only without any transformation.
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
        
        self.input_error = paint_text('INVALID ENTRY, ENTER AN INTEGER: ', self.colorset['warning'], print_trigger = False)

        try:
            self.new_i = int(self.new_i)
        except:
            while not isinstance(self.new_i, (int,float)):
                    
                self.new_i = input(self.input_error)
                
                try:
                    self.new_i = int(self.new_i)
                except:
                    pass
                  
        return self.new_i


    # this is a help function, do not call it when using a package.
    def _set_float(
        self,
        ) -> ReturnType:
        
        '''
        * converts input to float.
        '''

        self.input_error = paint_text('INVALID ENTRY, ENTER A FLOAT VALUE: ', self.colorset['warning'], print_trigger = False)

        try:
            self.new_i = float(self.new_i)
        except:
            while not isinstance(self.new_i, float):
                    
                self.new_i = input(self.input_error)
                
                try:
                    self.new_i = float(self.new_i)
                except:
                    pass
                  
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
    def _set_num_list(self, loop_break = 'X', activate_special = None):
        
        self.num_input = paint_text(f'ENTER A NUMBER OR ENTER {loop_break} TO QUIT: ', self.colorset['display_message'], print_trigger = False)
        self.input_error = paint_text('INVALID ENTRY, ENTER A NUMBER: ', self.colorset['warning'], print_trigger = False)
        self.save_confirm = paint_text('LIST SAVED WITH FOLLOWING CONTENTS: ', self.colorset['display_headline'], print_trigger = False)
        
        running = True

        num_list = []

        while running:
             
            tmp_user_input = input(self.num_input)
            
            try:
                user_input = float(tmp_user_input)
            except:
                user_input = tmp_user_input.upper()
            
            if str(user_input) == loop_break:
                print(self.save_confirm)
                running = False
                
            elif isinstance(user_input, (int, float)):
                num_list.append(float(user_input))
                print(num_list)
                
            else:
                while not isinstance(user_input, (int,float)):
                    
                    tmp_user_input = input(self.input_error)
            
                    try:
                        user_input = float(tmp_user_input)
                    except:
                        user_input = tmp_user_input.upper()
                        
                num_list.append(float(user_input))

        self.tmp_num_list = []
        
        for i in num_list:
            if str(i).endswith('.0'):
                i = int(i)
                self.tmp_num_list.append(i)
            else:
                self.tmp_num_list.append(i)
                
        if activate_special == '1d':
            self.tmp_num_list = np.array(self.tmp_num_list)
            
        if activate_special == '2d':
            self.tmp_num_list = np.array([self.tmp_num_list])
                
        paint_text(self.tmp_num_list, self.colorset['display_headline'])
        print('')

        return self.tmp_num_list
    
    
    # this is a help function, do not call it when using a package.
    def _set_str_list(self, loop_break = '0'):
        
        self.text_input = paint_text(f'ENTER A TEXT OR ENTER {loop_break} TO QUIT: ', self.colorset['display_message'], print_trigger = False)
        self.input_error = paint_text('INVALID ENTRY, ENTER A TEXT: ', self.colorset['warning'], print_trigger = False)
        self.save_confirm = paint_text('LIST SAVED WITH FOLLOWING CONTENTS: ', self.colorset['display_headline'], print_trigger = False)
        
        running = True
        
        str_list = []

        while running:
            user_input = input(self.text_input)
            
            if user_input == loop_break:
                print(self.save_confirm)
                running = False
                
            elif user_input.isalpha():
                str_list.append(str(user_input))
                print(str_list)
                
            else:
                while not user_input.isalpha():
                    user_input = input(self.input_error)
                str_list.append(str(user_input))
                print(str_list)
                
        self.tmp_str_list = str_list
        
        paint_text(self.tmp_str_list, self.colorset['display_headline'])
        print('')
        
        return self.tmp_str_list
    
    
    # this is a help function, do not call it when using a package.
    def _set_list(self, loop_break = 'dualityexit'):
        
        self._tmp_list_input = paint_text(f'ENTER ANY VALUE/TEXT OR ENTER {loop_break} TO QUIT: ', self.colorset['display_message'], print_trigger = False)
        self.save_confirm = paint_text('LIST SAVED WITH FOLLOWING CONTENTS: ', self.colorset['display_headline'], print_trigger = False)
        
        running = True
        
        initial_list = []

        while running:
            user_input = input(self._tmp_list_input)

            if user_input == loop_break:
                print(self.save_confirm)
                running = False
                
            else:
                try:
                    user_input = float(user_input)
                except:
                    pass
                    
                initial_list.append(user_input)
                print(initial_list)
                
        self._tmp_list = []
        
        for i in initial_list:
            if str(i).endswith('.0'):
                i = int(i)
                self._tmp_list.append(i)
            else:
                self._tmp_list.append(i)
        
        paint_text(self._tmp_list, self.colorset['display_headline'])
        print('')
        
        return self._tmp_list
    
    
    # this is a help function, do not call it when using a package.
    def _set_numpy_1darray(self):
        return self._set_num_list(loop_break = 'X', activate_special = '1d')
    

    # this is a help function, do not call it when using a package.
    def _set_numpy_2darray(self):
        return self._set_num_list(loop_break = 'X', activate_special = '2d')
    
    
    # this is a help function, do not call it when using a package.
    def _set_pandas_df(self):
        self.filepathinput = paint_text('ENTER THE FILE PATH: ', self.colorset['display_message'], print_trigger = False)
        self.availablecolumnsinput = paint_text('\nCOLUMNS PASSED TO DATAFRAME', self.colorset['display_headline'], print_trigger = False)
        self.filesupporterror = paint_text('=== ONLY CSV, XLSX AND JSON FILES SUPPORTED. ===\n', self.colorset['warning'], print_trigger = False)
        self.dataframeerror = paint_text('=== UNEXPECTED ERROR IN DATAFRAME CREATION. ===\n', self.colorset['warning'], print_trigger = False)
        self.dfsaved = paint_text('DATAFRAME SAVED.\n', self.colorset['display_headline'], print_trigger = False)
        
        file = input(self.filepathinput)
        file = file.replace("'", '"').strip('"')
        
        if str(file).endswith('.csv'):
            data = pd.read_csv(file)
            print(self.availablecolumnsinput)
            for col in data.columns:
                print(col)
                
        elif str(file).endswith('.xlsx'):
            data = pd.read_excel(file)
            print(self.availablecolumnsinput)
            for col in data.columns:
                print(col)
                
        elif str(file).endswith('.json'):
            data = pd.read_json(file)
            print(self.availablecolumnsinput)
            for col in data.columns:
                print(col)
                
        else:
            raise Exception(self.filesupporterror)
        
        print('')
        
        try:
            print(self.dfsaved)
            return data
        except:
            raise Exception(self.dataframeerror)
    
    
    # this is a help function, do not call it when using a package.
    def _set_pandas_columns(self, loopbreak = 'dualityexit'):
        
        self.filepathinput = paint_text('ENTER THE FILE PATH: ', self.colorset['display_message'], print_trigger = False)
        self.availablecolumnsinput = paint_text('\nAVAILABLE COLUMNS', self.colorset['display_headline'], print_trigger = False)
        self.filecolinput = paint_text('ENTER A COLUMN NAME OR ENTER dualityexit TO QUIT: ', self.colorset['display_message'], print_trigger = False)
        self.filecolinputerror = paint_text('COLUMN NAME NOT FOUND, TRY AGAIN: ', self.colorset['warning'], print_trigger = False)
        self.duplicateerror = paint_text('COLUMN ALREADY ADDED, AVOIDED A DUPLICATE.', self.colorset['warning'], print_trigger = False)
        self.filesupporterror = paint_text('=== ONLY CSV, XLSX AND JSON FILES SUPPORTED. ===\n', self.colorset['warning'], print_trigger = False)
        self.dataframeerror = paint_text('=== UNEXPECTED ERROR IN DATAFRAME CREATION. ===\n', self.colorset['warning'], print_trigger = False)
        self.dfsaved = paint_text('DATAFRAME SAVED.\n', self.colorset['display_headline'], print_trigger = False)
        
        file = input(self.filepathinput)
        file = file.replace("'", '"').strip('"')
        
        if str(file).endswith('.csv'):
            data = pd.read_csv(file)
            print(self.availablecolumnsinput)
            for col in data.columns:
                print(col)
                
        elif str(file).endswith('.xlsx'):
            data = pd.read_excel(file)
            print(self.availablecolumnsinput)
            for col in data.columns:
                print(col)
                
        elif str(file).endswith('.json'):
            data = pd.read_json(file)
            print(self.availablecolumnsinput)
            for col in data.columns:
                print(col)
                
        else:
            raise Exception(self.filesupporterror)
        
        print('')
        
        running = True
        tmp_cols = []
        
        while running:
            file_col = input(self.filecolinput).replace("'", '"').strip('"')
            
            if file_col == loopbreak:
                break
            
            elif file_col in data.columns:
                if file_col not in tmp_cols:
                    tmp_cols.append(file_col)
                else:
                    print(self.duplicateerror)
                    
            else:
                while file_col not in data.columns:
                    file_col = input(self.filecolinputerror)
                if file_col not in tmp_cols:
                    tmp_cols.append(file_col)
                else:
                    print(self.duplicateerror)
        
        try:
            data = data[tmp_cols]
            print(self.dfsaved)
            return data
        except:
            raise Exception(self.dataframeerror)
        
        
    # this is a help function, do not call it when using a package.
    def _set_path(self):
        self.filepathinput = paint_text('ENTER THE FILE PATH: ', self.colorset['display_message'], print_trigger = False)
        self.filepatherror = paint_text('=== UNEXPECTED ERROR OCCURED WHILE LOCATING THE PATH. ===\n', self.colorset['warning'], print_trigger = False)
        
        try:
            file = input(self.filepathinput)
            file = file.replace("'", '"').strip('"')
        except:
            raise Exception(self.filepatherror)
        
        return file
        
        
    # this is a help function, do not call it when using a package. (SCRIPT)
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
        self.script_error_input = []

        while self.iterate == True:
            
            self.option = input(self.display_message)
            
            if 'exit' in self.include:
                if self.option == self.break_key:
                    print('')
                    break
            
            while not self.option in self.option_names:
                
                self.option = input(paint_text('INVALID OPTION, ENTER THE OPTION: ', self.colorset['warning'], print_trigger = False))
                
                if self.option == self.break_key:
                    self.script_error_input += [self.option]
                    break

            if self.option not in self.script_error_input:
                self.tmp_name_list += [self.option]
                self.print_val_list += self.option
                
                if self.show_confirmation == True:
                    print(self.output_message, self.option + '\n')
                    
                self.tmp_list += [self.dictionary_menu[self.option]]
                self.tmp_print_list += [self.print_val_dict[self.option]]

        return self.tmp_list
    
    
    # this is a help function, do not call it when using a package. (WHEEL)
    def _wheel_queue_handler(
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
        self.wheel_error_input = []
            
        self.option = input(self.display_message)
          
        if 'exit' not in self.include:
            self.break_key = None
            
        if self.option == self.break_key:
            print('')
            paint_text(self.exit_message, self.colorset['exit_message'], print_trigger = True)
            exit()
                            
        while not self.option in self.option_names:
                
            if self.option == self.break_key:
                self.wheel_error_input += [self.option]
                break

            self.option = input(paint_text('INVALID OPTION, ENTER THE OPTION: ', self.colorset['warning'], print_trigger = False))
            
        if self.option not in self.wheel_error_input:
            print('')
            self.tmp_name_list += [self.option]
            self.print_val_list += self.option
            
            if self.show_confirmation == True:
                print(self.output_message, self.option + '\n')
                
            self.tmp_list += [self.dictionary_menu[self.option]]
            self.tmp_print_list += [self.print_val_dict[self.option]]
        
        return self.tmp_list


    # this is a help function, do not call it when using a package. (NO QUEUE)
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
        
        if self.show_confirmation == True:
            print(self.output_message, self.option + '\n')
            
        self.tmp_list += [self.dictionary_menu[self.option]]
        self.tmp_print_list += [self.print_val_dict[self.option]]

        return self.tmp_list


    # function that outputs available data types of _redefine function.
    def datatypes(
        self,
        print_trigger = True,
        ) -> ListType:
        
        '''
        * returns a dictionary of function argument transformation options. 
        '''
        
        self._redefine_dtypes_list = {
            'int': '-> single integer value.',
            'float': ' -> single float value.',
            'str': '-> single text value.',
            'list' : '-> list that supports both textual and numerical inputs.',
            'numlist' : '-> list that supports numerical inputs only.',
            'strlist' : '-> list that supports textual inputs only.',
            'np.1darray' : '-> list that supports numerical inputs only and transforms it into a numpy array of 1 dimension.',
            'np.2darray' : '-> list that supports numerical inputs only and transforms it into a numpy array of 2 dimensions.',
            'pd.df' : '-> creates a pandas dataframe from a whole file path file (.csv, .xlsx, .json).',
            'pd.columns' : '-> creates a pandas dataframe from a file path file with certain column/s only (.csv, .xlsx, .json).',
            'path' : '-> stores the file path only without any transformation.',
        }
        
        if print_trigger == True:
            
            print('')
            for k, v in self._redefine_dtypes_list.items():
                print(k, v)
            print('')
        
        return self._redefine_dtypes_list
