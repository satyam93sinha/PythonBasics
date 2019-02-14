Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import Fibonacci_Package
>>> Fibonacci_Package.fibo
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Fibonacci_Package.fibo
AttributeError: module 'Fibonacci_Package' has no attribute 'fibo'
>>> Fibonacci_Package.fibo()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Fibonacci_Package.fibo()
AttributeError: module 'Fibonacci_Package' has no attribute 'fibo'
>>> dir(Fibonacci_Package)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
>>> Fibonacci_Package.fib(40)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Fibonacci_Package.fib(40)
AttributeError: module 'Fibonacci_Package' has no attribute 'fib'
>>> Fibonacci_Package.Fibonacci.fib(50)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Fibonacci_Package.Fibonacci.fib(50)
AttributeError: module 'Fibonacci_Package' has no attribute 'Fibonacci'
>>> import Fibonacci_Package.fibo
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    import Fibonacci_Package.fibo
ModuleNotFoundError: No module named 'Fibonacci_Package.fibo'
>>> # so called ImportError
>>> import Fibonacci_Package.Fibonacci
>>> Fibonacci_Package.Fibonacci.fib(50)
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
>>> # we access package, module, functions in this way when __init__.py is not
>>> # initialized.
>>> 
