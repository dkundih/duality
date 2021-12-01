def menu():
    print('\n - duality Command Line Interface © David Kundih -\n')
    print('AVAILABLE FEATURES')
    print(' 1 | Monte Carlo Simulation')
    print(' 2 | Dijkstra algorithm')
    print(' 3 | Economic Order Quantity')
    print(' 4 | Exit')

#client.
def dualityCLI():
    while True:
        menu()
        choice = input('Choose an option: ')
        if choice == '1':
            MonteCarloCLI()
        if choice == '2':
            DijkstraCLI()
        if choice == '3':
            EOQCLI()
        if choice == '4':
            print('Exiting.')
            break

#MonteCarlo client extension.
def MonteCarloCLI():
    from duality.objects import MonteCarlo
    import pandas as pd
    file = input('File path: ').replace("'", '"').strip('"')
    if str(file).endswith('.csv'):
        data = pd.read_csv(file)
    elif str(file).endswith('.xlsx'):
        data = pd.read_excel(file)
    elif str(file).endswith('.json'):
        data = pd.read_json(file)
    else:
        raise Exception('Only csv, xlsx and json files supported.')
    file_col = input('Enter column name: ').replace("'", '"').strip('"')
    data = data[file_col]
    MC = MonteCarlo()
    simulations = int(input('Enter number of simulations: '))
    period = int(input('Enter desired period: '))
    executed = MC.execute(data, simulations, period)
    while True:
        action = input('ACTIONS: graph, change, values, stats, risk, hist, menu, help: ')
        if action == 'graph':
            MC.graph()
        elif action == 'change':
            print('1 | csv')
            print('2 | xlsx')
            print('3 | json')
            file_type = input('Enter the number of file type:')
            output = MC.get_change() 
            save_to(output, 'change', choice = file_type)
        elif action == 'values':
            print('1 | csv')
            print('2 | xlsx')
            print('3 | json')
            file_type = input('Enter the number of file type:')
            save_to(executed, 'values', choice = file_type)
        elif action == 'stats':
            MC.get_stats()
        elif action == 'risk':
            sample = int(input('Number of iterations: '))
            MC.get_risk(sample)
        elif action == 'hist':
            print('1 | Basic Histogram')
            print('2 | Empirical Rule Histogram')
            method = input('Enter histogram method: ')
            if method == '1':
                MC.hist()
            elif method == '2':
                MC.hist(method = 'e')
            else:
                print('Invalid method.')
        elif action == 'menu':
            break
        elif action == 'help':
            print('https://github.com/dkundih/duality')

def save_to(file, func_name, choice):
    import pandas as pd
    import os
    if choice == '1':
        extension = '.csv'
        file.to_csv('duality.MonteCarlo - ' + func_name + extension)
        print(os.path.join(os.getcwd() + '\duality.MonteCarlo - ' + func_name + extension))
    if choice == '2':
        extension = '.xlsx'
        file.to_excel('duality.MonteCarlo - ' + func_name + extension)
        print(os.path.join(os.getcwd() + '\duality.MonteCarlo - ' + func_name + extension))
    if choice == '3':
        extension = '.json'
        file.to_json('duality.MonteCarlo - ' + func_name + extension)
        print(os.path.join(os.getcwd() + '\duality.MonteCarlo - ' + func_name + extension))
    
#Dijkstra client extension.
def DijkstraCLI():
    from duality.objects import Dijkstra
    pass

#EOQ client extension.
def EOQCLI():
    from duality.objects import EOQ
    pass

#runs client.
if __name__ == '__main__':
    dualityCLI()
