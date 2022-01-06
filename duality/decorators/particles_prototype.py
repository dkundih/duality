function_mapping = {}

def record_function(func):
    function_mapping[func.__name__] = func

    def _wrap(*args, **kwargs):
        return func(*args, **kwargs)

    return _wrap


@record_function
def example1():
    return 1


@record_function
def example2():
    return 2


@record_function
def example3():
    return 3

entry = input('Enter the function name: ')
function = function_mapping[entry]
print(function())


'''

so, as the function is being saved into the dict. it can just be accessed and called

using that func.__name__  as the key, rather than a value

so now function_mapping is a string(key) -> function(value)


'''