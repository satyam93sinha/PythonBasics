def timer(timer_function):
    def wrapper(*args):
        import time
        start_time=time.time()
        func=timer_function()
        end_time=time.time()
        print(end_time-start_time)
        return func
    return wrapper
@timer
def fib_list(num):
    l=[]
    a,b=0,1
    l.append(a)
    for __in range(num-1):
        a,b=b,b+a
        l.append(a)
    return l
@timer
def fib_gen(num):
    a,b=0,1
    for __ in range(num):
        yield a
        a,b=b,b+a

print(list(fib_gen(10)))
print(list(fib_list(10)))
