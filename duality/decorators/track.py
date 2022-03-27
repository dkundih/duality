# makes multiple instances of the object available.
from duality.plugins.metaclass import Meta

from duality.plugins.types import (
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
)

# tracks function behaviuor and stores it into a JSON file.
# --- DEPRECATED ---
class Track(metaclass = Meta):

    # func_name - stores a function name it assigns to a JSON related object afterwards.
    # -
    # appends to a function and tracks it's execution details.
    # DEFAULT: track.entry(func_name).
    def entry(
        func_name : StringType = 'placeholder_name',
        ) -> StringDictionary:
        def log(func):
                import sys
                import json
                import datetime

                def logsaver(*args, **kwargs):
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
                return logsaver

        return log

    # style ('decorator' - appends to a function.)
    # style ('function' - executes as a standalone function.)
    # return_option ('logs' - executes the function, but returns logs.)
    # return_option ('function' - shows logs, but returns the function - THIS DOES NOT RETURN THE LAST ENTRY FROM LOGS!!!)
    # -
    # outputs the saved JSON file entries.
    # DEFAULT: track.display(style = 'decorator', return_option = 'logs').
    def display(
        style : StringType = 'decorator', 
        return_option : StringType = 'logs',
        ) -> ReturnType:
        if style == 'function':
            f = open('Logs.json', 'r')
            print(f.read())

        elif style == 'decorator':
            if return_option == 'logs':
                def wrapper(func):
                    def decorator(*args, **kwargs):
                        f = open('Logs.json', 'r')
                        func(*args, **kwargs)
                        logs = print(f.read())
                        return logs
                    return decorator

                return wrapper

            elif return_option == 'function':
                def wrapper(func):
                    def decorator(*args, **kwargs):
                        f = open('Logs.json', 'r')
                        print(f.read())
                        return func(*args, **kwargs)
                    return decorator

                return wrapper
