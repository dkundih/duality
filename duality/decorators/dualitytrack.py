# makes multiple instances of the object available.
from logistics.plugins.metaclass import Meta

# imports all data types.
from logistics.plugins.types import *

# imports coloring.
from logistics.plugins.coloring import *

# dependencies import.
import sys
import json
import datetime

class DualityTrack(metaclass = Meta):

    '''
    * tracks function behaviuor and stores it into a JSON file.
    | DEPRECATED |
    '''

    def entry(
        func_name : StringType = 'placeholder_name',
        ) -> StringDictionary:

        '''
        * appends to a function and tracks it's execution details.

        - func_name - stores a function name it assigns to a JSON related object afterwards. 
        # DEFAULT: track.entry(func_name).
        '''

        def _log(func):

                def _logsaver(*args, **kwargs):
                    start = datetime.datetime.now()
                    results = func(*args, **kwargs)
                    end = datetime.datetime.now()
                    func_name =  {
                            'EXECUTION TIME: ' : str(end - start),
                            'EXECUTED AT: ' : str(datetime.datetime.now()),
                            'MEMORY SIZE: ' : str(sys.getsizeof(func)) + ' bytes',
                            },

                    with open('Logs.json', 'a') as f:
                        f.write(json.dumps(func_name, indent = 4)),
                        f.write(',\n')
                        f.close()
                        return results
                return _logsaver

        return _log

    def display(
        style : StringType = 'decorator', 
        return_option : StringType = 'logs',
        ) -> ReturnType:

        '''
        * outputs the saved JSON file entries.
        
        - style ('decorator' - appends to a function.)
        - style ('function' - executes as a standalone function.)
        - return_option ('logs' - executes the function, but returns logs.)
        - return_option ('function' - shows logs, but returns the function - THIS DOES NOT RETURN THE LAST ENTRY FROM LOGS!!!)
        # DEFAULT: track.display(style = 'decorator', return_option = 'logs').
        '''

        if style == 'function':
            f = open('Logs.json', 'r')
            print(f.read())

        elif style == 'decorator':
            if return_option == 'logs':
                def _wrapper(func):
                    def _decorator(*args, **kwargs):
                        f = open('Logs.json', 'r')
                        func(*args, **kwargs)
                        logs = print(f.read())
                        return logs
                    return _decorator

                return _wrapper

            elif return_option == 'function':
                def _wrapper(func):
                    def _decorator(*args, **kwargs):
                        f = open('Logs.json', 'r')
                        print(f.read())
                        return func(*args, **kwargs)
                    return _decorator

                return _wrapper
