'''

This is a connection to the main folder of the duality library.

AVAILABLE MODULES IN THE LIBRARY:

	TOOLKIT
	-------

	duality.toolkit is a set of data manipulation tools that can be directly accessed from the main module as duality.function()
		print(help(duality.toolkit)) in order to see available features.

	MONTECARLO
	----------

	duality.MonteCarlo is a module for performing the Monte Carlo simulation over the defined data with a lot of useful features.
		print(help(duality.MonteCarlo)) in order to see available features.

	EOQ
	---
	
	duality.EOQ is a module for finding an Economic order quantity over the defined data with a lot of useful features.
		print(help(duality.EOQ)) in order to see available features.

'''

#ignore __pycache__ from forming inside the library directory.
import sys
sys.dont_write_bytecode = True

#imports essential functions from the duality library.
from duality.hub import toolkit
from duality.hub.toolkit import *
from duality.objects.eoq import EOQ
from duality.objects.montecarlo import MonteCarlo
from duality.misc._meta import (
	__author__,
	__copyright__,
	__credits__,
	__license__,
	__version__,
	__documentation__,
	__contact__,
	__donate__
)

#all relevant contents.
__all__ = [
	toolkit,
	MonteCarlo,
	EOQ,
]