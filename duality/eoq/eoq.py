#object that contains the calculation data.
class EOQ:

    '''
    
    (OBJECT INFO)
    ---
    duality.EOQ - main class that defines the data needed for the calculation.
        * takes 4 additional arguments.
            annual_demand_quantity - integer of demanded quantity in a year.
            order_fixed_cost - integer or float presenting the fixed cost of the order.
            annual_holding_cost - cost of holding the goods in a year.
            log_summary (default: log_summary = False) - event log of executed functions.
        * automatically executes the .execute() function.

    duality.EOQ CALLABLE FUNCTIONS:

        .execute() - executes the calculation of EOQ over the defined parameters.
            *is automatically executed with the Object setup.

        .get_logs() - shows the event log of executed functions.
            * takes no additional arguments.
            * Requirements:
                log_summary = True.

    '''

    #metadata of the used package.
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
 
    #initial value configuration.
    def __init__(self, annual_demand_quantity, order_fixed_cost, annual_holding_cost, log_summary = False):
        self.annual_demand_quantity = annual_demand_quantity
        self.order_fixed_cost = order_fixed_cost
        self.annual_holding_cost = annual_holding_cost
        self.log_summary = log_summary
        print(f'EOQ has been set up with annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.')
        self.execute()
        
    #creates an event log that tracks the function execution time and duration.
    def classLog(func_name):
        def log(func):
                import time
                import datetime
                def logsaver(self, *args, **kwargs):
                    if self.log_summary == True:
                        start = time.time()
                        results = func(self, *args, **kwargs)
                        with open('duality Logs.txt', 'a') as f:
                            f.write('Performed a function ' + func_name + ' at: ' + str(datetime.datetime.now()) + '.' + ' Time spent performing the action: ' + str(time.time() - start) + ' seconds.' + '\n')
                            return results
                    else:
                            results = func(self, *args, **kwargs)
                            return results
                return logsaver
        return log
        
    @classLog('__str__()')
    #class information.
    def __str__(self):
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    @classLog('__repr__()')
    #class information.
    def __repr__(self):
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    @classLog('execute() - built in function.')
    #executes the calculation of EOQ over the defined parameters.
    def execute(self):
        import math 
        eoq = math.sqrt((((2 * self.annual_demand_quantity) * self.order_fixed_cost) / self.annual_holding_cost))
        print('EOQ is: ', eoq)
        return eoq

    @classLog('get_logs()')
    #returns the saved logs of executed functions.
    def get_logs(self):
        f = open('duality Logs.txt', 'r')
        print(f.read())