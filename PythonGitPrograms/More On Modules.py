Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import FibonacciReturn
>>> FibonacciReturn.fibonacci_return(25)
[0, 1, 1, 2, 3, 5, 8, 13, 21]
>>> FibonacciReturn.fibonacci_return
<function fibonacci_return at 0x03454540>
>>> import Fibonacci
>>> Fibonacci.fib(50)
Fibonacci series:
0 
 1
0
1
1
2
3
5
8
13
21
34
>>> import Fibonacci
>>> Fibonacci.fib(50)
Fibonacci series:
0 
 1
0
1
1
2
3
5
8
13
21
34
>>> import importlib; importlib.reload(Fibonacci)
<module 'Fibonacci' from 'G:\\Softwares\\Python 3.7.0\\Fibonacci.py'>
>>> Fibonacci.fib(50)
Fibonacci series:
0
1
1
2
3
5
8
13
21
34
>>> # the above statement shows how to reload the imported module when
>>> #      something has been changed in previous module with interpreter open
>>> #      Either interpreter could be reopened or we can do as above.
>>> #   importlib is a library, reload() would be a function, we pass
>>> #       modified module name to reload() funcn as argument.
>>> Fibonacci.fibonacci(50)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> # list is returned from fibonacci() funcn of Fibonacci module.
>>> # With Fibonacci module imported, we can access all defined within it.
>>> import Fibonacci as fibo
>>> fibo.fib(50)
Fibonacci series:
0
1
1
2
3
5
8
13
21
34
>>> from Fibonacci import fib
>>> fib(550)
Fibonacci series:
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
>>> fibonacci(30)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    fibonacci(30)
NameError: name 'fibonacci' is not defined
>>> # bcoz module isn't imported, just the fib funcn has been.
>>> from Fibonacci import *
>>> fibonacci(50)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> 
