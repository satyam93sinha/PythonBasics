Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from Fibonacci_Package import *
>>> from Fibonacci_Package.Fibonacci import *
>>> fib(50)
Fibonacci series: fib(n): 
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
>>> fibonacci_return(50)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fibonacci_return(50)
NameError: name 'fibonacci_return' is not defined
>>> FibonacciReturn.fibonacci_return(50)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    FibonacciReturn.fibonacci_return(50)
NameError: name 'FibonacciReturn' is not defined
>>> # from Fibonacci_Package import * doesn't import as we expect it to.
>>> import importlib
>>> importlib.reload(Fibonacci_Package)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    importlib.reload(Fibonacci_Package)
NameError: name 'Fibonacci_Package' is not defined
>>> from Fibonacci_Package import *
>>> fibonacci_return(50)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fibonacci_return(50)
NameError: name 'fibonacci_return' is not defined
>>> FibonacciReturn.fibonacci_return(40)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    FibonacciReturn.fibonacci_return(40)
NameError: name 'FibonacciReturn' is not defined
>>> 
