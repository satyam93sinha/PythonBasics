Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import Fibonacc
>>> fib(50)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fib(50)
NameError: name 'fib' is not defined
>>> dir(Fibonacc)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'fib', 'fibonacci', 'fibonacci_return']
>>> Fibonacci.fib(50)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Fibonacci.fib(50)
NameError: name 'Fibonacci' is not defined
>>> Fibonacc.fib(50)
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
>>> Fibonacc.fibonacci_return(50)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> Fibonacc.fibonacci(50)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> import importlib
>>> importlib.reload(Fibonacci_Package)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    importlib.reload(Fibonacci_Package)
NameError: name 'Fibonacci_Package' is not defined
>>> import Fibonacci_Package
>>> Fibonacci_Package.fib(40)
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
>>> Fibonacci_Package.fibonacci(40)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> Fibonacci_Package.fibonacci_return(40)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> # importlib.reload() works only with modules, not packages.
>>> Fibonacci_Package.fibo(3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Fibonacci_Package.fibo(3)
AttributeError: module 'Fibonacci_Package' has no attribute 'fibo'
>>> Fibonacci_Package.fibo
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Fibonacci_Package.fibo
AttributeError: module 'Fibonacci_Package' has no attribute 'fibo'
>>> import Fibonacci_Package
>>> Fibonacci_Package.__doc__
>>> print(Fibonacci_Package.__doc__)
None
>>> Fibonacci_Package.__cached__
'G:\\Softwares\\Python 3.7.0\\Fibonacci_Package\\__pycache__\\__init__.cpython-37.pyc'
>>> # displays the path where its compiled version is cached, inside __pycache__
>>> 
Fibonacci_Package.fib(40)
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
>>> importlib.reload(__init__.py)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    importlib.reload(__init__.py)
NameError: name '__init__' is not defined
>>> importlib.reload(Fibonacci_Package)
<module 'Fibonacci_Package' from 'G:\\Softwares\\Python 3.7.0\\Fibonacci_Package\\__init__.py'>
>>> Fibonacci_Package.fib(50)
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
>>> Fibonacci_Package.fibo
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    Fibonacci_Package.fibo
AttributeError: module 'Fibonacci_Package' has no attribute 'fibo'
>>> 
