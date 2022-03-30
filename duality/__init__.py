'''

duality - Decorator particles for creating an executable menu from a python file and function execution tracking.
=====================================================================

This is a connection to the __init__ file of the duality package.

AVAILABLE FEATURES IN THE PACKAGE:

	record (OBJECT/DECORATOR)
	-------------------

	duality.Record is an object decorator class that stores menu options over functions and class methods for listing and executing in a CLI.
		print(help(duality.Record)) in order to see available features.

	track (OBJECT/DECORATOR)
	------------

	duality.Track is an object decorator class that tracks function behaviuor and stores it into a JSON file.
		print(help(duality.Track)) in order to see available features.

'''

# ignore __pycache__ from forming inside the library directory.
import sys

from duality.plugins.types import AnyType
sys.dont_write_bytecode = True

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

# import types.
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

# all types.
__types__ = [
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
    AnyType
]

# imports relevant contents.
from duality.plugins.metaclass import Meta
from duality.decorators.record import Record
from duality.decorators.track import Track

# all relevant contents.
__all__ = [
	'Meta',
	'Record',
	'Track',
]
