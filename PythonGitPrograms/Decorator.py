def my_decorator(some_function):
    def wrapper():
        print('I am in wrapper')
        some_function()
        print('After some_function')
    return wrapper
def print_function():
    print('Print anything, testing how decorators work')
    
my_function=my_decorator(print_function)
my_function()
