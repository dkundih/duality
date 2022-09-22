### TEST ENV ###

# global duality import.
import duality

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


app = duality.DualityApp()

# package.
class MonteCarlo:

    @app.entry('init')
    def __init__(
        self, 
        list_of_values : NumberVectorAlike = app.store('list_of_values', 'numlist', 'VALUES'), 
        time_seq : IntegerType = app.store('time_seq', 'int'), 
        num_sims : IntegerType = app.store('num_sims', 'int'),
        ref_col : IntegerType = 0, 
        ref_row : IntegerType = 0,
        ) -> ReturnType:

        '''
        * initial launch.
        '''

        self.list_of_values = list_of_values
        self.time_seq = time_seq
        self.num_sims = num_sims
        self.ref_col = ref_col
        self.ref_row = ref_row

        return 

    @app.entry('execute', print_val = True)
    def execute(
        self,
        filtered : BooleanType = True,
        ) -> NumberArrayAlike:

        '''
        * executes a Monte Carlo simulation on a defined data set.
        - filtered (True/False) - filters the data setup print and warnings.
        # DEFAULT: MonteCarlo.execute(filtered : BooleanType = True.)
        '''

        if filtered == False:
            print(Fore.GREEN + f'Monte Carlo has been set up for {self.num_sims} simulations in a period of {self.time_seq} time measurement units and executed.' + Fore.RESET)
            print(Fore.RED + 'NOTE: Use data with reasonable standard deviation in order to prevent exponential growth of the function that cannot be plotted properly, recognize such abnormal values by a + sign anywhere in the data executed below.' + Fore.RESET)
        
        import numpy as np
        import pandas as pd

        # this removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
        # end of pandas warning removal block.

        try:
            self.list_of_values = pd.DataFrame(self.list_of_values)
            self.list_of_values = self.list_of_values.iloc[:, self.ref_col]
        except:
            raise KeyError('Impossible to reach a defined key, value pair. Data types supported: dictionary, list, numpy array, pandas DataFrame. Make sure to set index row_col on an existing field. Must be of type: int.')

        today_value = self.list_of_values.iloc[self.ref_col]
        data = pd.DataFrame()
        loading = 0

        for num_sim in range(self.num_sims):
            rand_change = self.list_of_values.pct_change().std()
            count = 0
            index_array = []
            index_array += [today_value + (today_value * np.random.normal(0, rand_change))]

            for num_day in range(self.time_seq):
                rand_change = self.list_of_values.pct_change().std()
                if count == self.time_seq:
                    break
                index_array += [index_array[count] + (today_value * np.random.normal(0, rand_change))]
                count += 1

            loading += 1
            print(end = '\r')
            print(loading, 'iterations out of', self.num_sims, 'executed so far', end = '')

            data[num_sim] = index_array
        print(end = '\r')
        print(Fore.GREEN + 'Monte Carlo simulation set up and ready to plot.' + Fore.RESET)
        self.results = data

        return data

    @app.entry('change', print_val = True)
    def get_change(
        self,
        ) -> NumberArrayAlike:

        '''
        * shows the percentage of Monte Carlo simulation value change for every iteration.
        '''

        return self.results.pct_change()

    
if __name__ == '__main__':
    app.wheel()
