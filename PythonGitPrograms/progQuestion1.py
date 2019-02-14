def length_decorator_check(some_function):
    if (args.length>10):
        raise LengthError('More than ten is not allowed')

@length_decorator_check
def display_list_passed(*args):
    for arg in args:
        print(arg)
display_list_passed(1,2,3)
