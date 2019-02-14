Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class MyEmptyClass:
	pass
yes its  a pass but why?
SyntaxError: invalid syntax
>>> def initlog:
	
SyntaxError: invalid syntax
>>> 
>>> def anything(*args):
	pass
'pass here asks to implement this function'
SyntaxError: invalid syntax
>>> type(pass)
SyntaxError: invalid syntax
>>> def fibonacci(n):
	#a,b=0,1
	for i in range(n):
		print(a)
		a,b=b,b+a

		
>>> fibonacci(5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    fibonacci(5)
  File "<pyshell#14>", line 4, in fibonacci
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment
>>> def fibonacci(n):
	a,b=0,1
	for i in range(n):
		print(a)
		a,b=b,b+a

		
>>> fibonacci(5)
0
1
1
2
3
>>> fibonacci(10)
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
>>> def fibonacci(n):
	"fibonacci(n) starts here, taking n as formal parameter."
	a,b=0,1
	"""for loop counter i increments until range(n) is reached,
	loop is exhausted to terminate the loop."""
	for i in range(n):
		print(a)
		a,b=b,b+a
	""" for loop exhausted, is terminated."""
	#Multi-lines string here are called as documentation strings/docstrings.

	
>>> fibonacci(10)
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
>>> def fibonacci(n):
	"fibonacci(n) starts here, taking n as formal parameter."
	a,b=0,1
	"""for loop counter i increments until range(n) is reached,
	loop is exhausted to terminate the loop."""
	for i in range(n):
		print(a,end=' ')
		a,b=b,b+a
	""" for loop exhausted, is terminated."""
	#Multi-lines string here are called as documentation strings/docstrings.

	
>>> fibonacci(10)
0 1 1 2 3 5 8 13 21 34 
>>> fibonacci
<function fibonacci at 0x0000023A41299510>
>>> type(fibonacci())
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    type(fibonacci())
TypeError: fibonacci() missing 1 required positional argument: 'n'
>>> type(fibonacci(2))
0 1 <class 'NoneType'>
>>> type(fibonacci)
<class 'function'>
>>> 
