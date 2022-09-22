### TEST ENV ###
import duality

a = duality.DualityApp()

@a.entry('strtest','shows the entries')
def show(entries = a.store('entries', 'strlist', 'ENTRIES')):
    for i in entries:
        print(i)
    return entries

@a.entry('numtest','shows the entries', print_val = True)
def show(entries = a.store('entries', 'numlist', 'ENTRIES')):
    result = sum(entries)
    return result

a.wheel(type = 'static')
