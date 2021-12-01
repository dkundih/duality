#main menu.
def menu():
    print('\n = duality Command Line Interface © David Kundih. =')
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
    file = input('File destination (without quotation marks): ')
    if str(file).endswith('.csv'):
        data = pd.read_csv(file)
    elif str(file).endswith('.xlsx'):
        data = pd.read_excel(file)
    elif str(file).endswith('.json'):
        data = pd.read_json(file)
    else:
        print('Only csv, xlsx and json files supported.')
    file_col = input('Enter column name (without quotation marks): ')
    data = data[file_col]
    MC = MonteCarlo()
    simulations = int(input('Enter number of simulations: '))
    period = int(input('Enter desired period: '))
    MC.execute(data, simulations, period)
    while True:
        action = input('Actions: graph, change, stats, risk, hist, menu, help: ')
        if action == 'graph':
            MC.graph()
        if action == 'change':
            print('Unavailable outside of IPython Notebook.')
            MC.get_change()
        if action == 'stats':
            MC.get_stats()
        if action == 'risk':
            sample = int(input('Number of iterations: '))
            MC.get_risk(sample)
        if action == 'hist':
            MC.hist()
        if action == 'menu':
            break
        if action == 'help':
            print(help(MonteCarlo))

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
