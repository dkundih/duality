'''

duality - Decorator particles for creating an executable menu from a python file and function execution tracking.
=====================================================================

This is a connection to the __init__ file of the duality package.

AVAILABLE FEATURES IN THE PACKAGE:

	dualityapp (OBJECT/DECORATOR)
	-------------------

	duality.DualityApp is an object decorator class that stores menu options over functions and class methods for listing and executing in a CLI.
		print(help(duality.DualityApp)) in order to see available features.
  
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

    DATATYPES (self._redefine_dtypes_list template)
    ________

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

	track (OBJECT/DECORATOR)
	------------

	duality.DualityTrack is an object decorator class that tracks function behaviuor and stores it into a JSON file.
		print(help(duality.DualityTrack)) in order to see available features.

'''

# ignore __pycache__ from forming inside the library directory.
import sys
import os
sys.dont_write_bytecode = True

# coloring.
from colorama import (
    Fore,
    Back,
    Style,
    init,
)

init()

# imports meta data.
from duality.misc._meta import (
    __author__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __documentation__,
    __contact__,
    __donate__,
)

# imports all data types.
from logistics.plugins.types import *

# imports coloring.
from logistics.plugins.coloring import *

# imports relevant dependencies.
from logistics.plugins.metaclass import Meta

# imports relevant contents.
from duality.decorators.dualityapp import DualityApp
from duality.decorators.dualitytrack import DualityTrack

# metaclass.
metaclass = [
    'Meta',
]

# all relevant contents.
__all__ = [
	'VandalTypes',
	'Meta',
	'DualityApp',
	'DualityTrack',
]
