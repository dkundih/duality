#object that contains the simulation data.
class MonteCarlo:

    '''

    (OBJECT INFO)
    --- 
    duality.MonteCarlo - main class that defines the data, desired time sequence and number of simulations.
        * takes 5 additional arguments.
            list_of_values - pandas dataframe of values.
            time_seq - desired time sequence.
            num_sims - desired number of simulation iterations.
            log_summary (default: log_summary = False) - event log of executed functions.
        * Requirements:
            pandas Python module.
            pd.DataFrame() defined data set.
        * automatically executes the .execute() function.

    duality.MonteCarlo CALLABLE FUNCTIONS:

        .execute() - executes a Monte Carlo simulation on a defined data set.
            *is automatically executed with the Object setup.

        .graph() - plots the Monte Carlo simulation on a graph.
            * takes 4 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10)).
                graph_title - title of the graph.
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.

        .get_risk() - calculates the risk of value decrease over time.
            * takes 1 optional argument (default: risk_sims = 5000).

        .get_stats() - shows the statistics of the Monte Carlo simulation.
            * takes no additional arguments.

        .get_logs() - shows the event log of executed functions.
            * takes no additional arguments.
            * Requirements:
                log_summary = True.
        
        .get_change() - shows the percentage of Monte Carlo simulation value change for every iteration.
            * takes no additional arguments.

        .hist() - plots the histogram of Monte Carlo simulation.
            * takes 5 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), method = 'b').
            If method = 'e' is chosen, no customization arguments apply.
                graph_title - title of the graph
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.
                method - default method is Basic histogram and it's performed by automation. In order to plot Empirical rule histogram add method = 'e' as the last argument. - NOTE: method of a histogram must be placed within quotation marks.
            * automatically executes the .get_stats(filtered = True) function in order to get standard deviation for the Empirical rule plotting.

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
    def __init__(self, list_of_values, time_seq, num_sims, ref_value_index = 0, log_summary = False): 
        self.list_of_values = list_of_values
        self.time_seq = time_seq
        self.num_sims = num_sims
        self.log_summary = log_summary
        self.ref_value_index = ref_value_index
        print(f'Monte Carlo has been set up for {self.num_sims} simulations in a period of {self.time_seq} time measurement units.')
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
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    @classLog('__repr__()')
    #class information.
    def __repr__(self):
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    @classLog('execute() - built in function.')
    #executes a Monte Carlo simulation on a defined data set.
    def execute(self):
            from duality.hub.hub import random_value
            print('Monte Carlo simulation has been executed')
            print('NOTE: Use data with reasonable standard deviation in order to prevent exponential growth of the function that cannot be plotted properly, recognize such abnormal values by a + sign anywhere in the data executed below.\nThe model that will be able to handle big standard deviations is currently being worked on, thank you for your patience.\n')
            import pandas as pd
            #This removes pandas warning of highly fragmented DataFrame for newer pandas versions.
            from warnings import simplefilter
            simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
            #End of pandas warning removal block.
            today_value = self.list_of_values.iloc[self.ref_value_index]
            data = pd.DataFrame()
            loading = 0

            for num_sim in range(self.num_sims):
                rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
                count = 0
                index_array = []
                simulated_index = today_value * (1 + rand_change)
                index_array.append(simulated_index)
                
                if simulated_index > (index_array[-1] * 2):
                    raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation cannot be executed properly.')
                        
                for num_day in range(self.time_seq):   
                    rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
                    if count == self.time_seq:
                        break
                    simulated_index = index_array[count] * (1 + rand_change)
                    index_array.append(simulated_index)
                    count += 1

                    if simulated_index > (index_array[-1] * 2):
                        raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation function cannot be executed properly.')
                
                loading +=1
                print(end='\r')
                print(loading, 'iterations out of', self.num_sims, 'executed so far', end = '')
                
                data[num_sim] = index_array
            print(end='\r')
            print('Monte Carlo simulation set up and ready to plot.')
            self.results = data
            return data

    @classLog('get_change()')
    #shows the percentage of Monte Carlo simulation value change for every iteration.
    def get_change(self):
        return self.results.pct_change()
   
    @classLog('get_risk()')
    #calculates the risk of negative values occuring.
    def get_risk(self, risk_sims = 5000):
        import random
        import pandas as pd
        #This removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
        #End of pandas warning removal block.
        today_value = self.list_of_values.iloc[self.ref_value_index]
        percent_change = self.list_of_values.pct_change()
        data = pd.DataFrame()
        smaller = []

        for num_sim in range(risk_sims): 
            random_change = random.choice(percent_change)
            index_array = []

            simulated_index = today_value * (1 + (random_change))
            index_array.append(simulated_index)
            data[num_sim] = index_array

            for sim in data[num_sim]:
                if sim < today_value:
                    smaller.append(sim)
        NRisk = len(smaller) / num_sim * 100

        assert (NRisk < 100), 'Time sequence and/or number of iterations are too low for the proper risk calculation.'

        print('Risk for this option is', round(NRisk,2), '%.')
     
    @classLog('graph()')
    #plots the Monte Carlo simulation on a graph.   
    def graph(self, graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10)):
        print('MonteCarlo() plotting initialized.')
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('duality (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')
        plt.suptitle(graph_title, fontsize = 25, weight = 'bold')
        plt.plot(self.results)
        plt.axhline(y = self.results[0][0], color = 'k', linestyle = 'solid')
        plt.xlabel(x_title, fontsize = 18, weight = 'semibold')
        plt.ylabel(y_title, fontsize = 18, weight = 'semibold')
        plt.show()
        print('MonteCarlo() plotting finished.')
   
    @classLog('get_stats()')
    #shows the statistics of the Monte Carlo simulation.
    def get_stats(self, filtered = False): 
        import numpy as np
        mean_value = np.mean(self.results.loc[self.time_seq])
        mean_value = round((mean_value),2)
        standard_deviation = round(np.std(self.results.loc[self.time_seq]),2)
        standard_deviation = round((standard_deviation),2)
        maximum_value = np.max(self.results.loc[self.time_seq])
        maximum_value = round((maximum_value),2)
        minimum_value = np.min(self.results.loc[self.time_seq])
        minimum_value = round((minimum_value),2)
        self.standard_deviation = standard_deviation
        self.mean_value = mean_value
        if filtered == False:
            print('Number of simulations: ', self.time_seq)
            print('Number of iterations: ', self.num_sims)
            print('Mean value: ', mean_value)
            print('Standard deviation: ', standard_deviation)
            print('Maximum: ', maximum_value)
            print('Minimum: ', minimum_value)


    @classLog('hist()')
    #plots the histogram of Monte Carlo simulation.
    def hist(self, graph_title = 'Histogram of value frequencies', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), **method):
        self.get_stats(filtered = True)
        std_plus = self.mean_value + self.standard_deviation
        std_minus = self.mean_value - self.standard_deviation
        std_plus2 = self.mean_value + (self.standard_deviation * 2)
        std_minus2 = self.mean_value - (self.standard_deviation * 2)
        std_plus3 = self.mean_value + (self.standard_deviation * 3)
        std_minus3 = self.mean_value - (self.standard_deviation * 3)

        if self.time_seq > 50:
            print('NOTE: Time sequence defined greatly impacts the lenght of histogram plotting.\n') 

        print('Histogram plotting initiated...')
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('duality (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')

        if method.get("method") != "e":
            print('CHOSEN METHOD: Basic histogram model.')
            plt.suptitle(graph_title, fontsize = 25, weight = 'bold')
            
        if method.get("method") == "e":

            print('CHOSEN METHOD: Empirical rule.')
            plt.suptitle('Value division based on the Empirical rule', fontsize = 25, weight = 'bold')
            plt.axvline(x = std_plus, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus, color = 'r', linestyle = 'dashed')
            plt.axvline(x = self.mean_value, color = 'k', linestyle = 'solid')
            plt.axvline(x = std_plus2, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus2, color = 'r', linestyle = 'dashed')
            plt.axvline(x = std_plus3, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus3, color = 'r', linestyle = 'dashed')
        plt.hist(self.results, bins = self.time_seq , ec = 'm')
        plt.xlabel(x_title, weight = 'semibold')
        plt.ylabel(y_title, weight= 'semibold')
        plt.show()
        print('Histogram plotting finished.')

    @classLog('get_logs()')
    #returns the saved logs of executed functions.
    def get_logs(self):
        f = open('duality Logs.txt', 'r')
        print(f.read())