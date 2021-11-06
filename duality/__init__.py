'''

This is a connection to the main folder of the duality package.

AVAILABLE MODULES IN THE PACKAGE:

	HUB
	---
	duality.hub is a hub of data manipulation tools.
		print(help(duality.hub)) in order to see available features.

	MONTECARLO
	---
	duality.MonteCarlo is a module for performing the Monte Carlo simulation over the defined data with a lot of useful features.
		print(help(duality.MonteCarlo)) in order to see available features.

	EOQ
	---
	duality.EOQ is a module for finding an Economic order quantity over the defined data with a lot of useful features.
		print(help(duality.EOQ)) in order to see available features.

'''

#ignore __pycache__ from forming inside the package directory.
import sys
sys.dont_write_bytecode = True

#imports essential functions from the duality package.
from duality.eoq.eoq import EOQ
from duality.hub import hub
from duality.hub.hub import *
from duality.montecarlo.montecarlo import MonteCarlo
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
