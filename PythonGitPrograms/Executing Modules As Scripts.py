Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> python Fibonacci.py
SyntaxError: invalid syntax
>>> python
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> Fibonacci.py
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Fibonacci.py
NameError: name 'Fibonacci' is not defined
>>> Fibonacci.py 50
SyntaxError: invalid syntax
>>> import Fibonacci
>>> Fibonacci.fibonacci(30)
[0, 1, 1, 2, 3, 5, 8, 13, 21]
>>> Fibonacci 40
SyntaxError: invalid syntax
>>> 
============== RESTART: G:\Softwares\Python 3.7.0\Fibonacci.py ==============
Traceback (most recent call last):
  File "G:\Softwares\Python 3.7.0\Fibonacci.py", line 30, in <module>
    fibonacci(int(sys.argv[1]))
IndexError: list index out of range
>>> 
