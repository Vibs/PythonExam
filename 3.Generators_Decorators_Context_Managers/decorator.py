
def debugger(func_to_debug):
    def wrapper(*args):
        print(f'DEBUG: func: {func_to_debug.__name__}')
        print(f'DEBUG: args: {args}')
        result = func_to_debug(*args)
        print(f'RESULT: {result}')
        return result
    return wrapper


@debugger
def add(a, b):
    return a + b


add(5, 6)


