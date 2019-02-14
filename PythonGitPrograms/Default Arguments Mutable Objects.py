Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f(a,L=[]):
	L.append(a)
	return L

>>> print(f(1))
[1]
>>> f(3)
[1, 3]
>>> f(2)
[1, 3, 2]
>>> def f(a,L is NONE):
	
SyntaxError: invalid syntax
>>> def f(a,L=NONE):
	if L is NONE:
		L=[]
		L.append(a)
		return L

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    def f(a,L=NONE):
NameError: name 'NONE' is not defined
>>> def f(a,L=None):
	if L is None:
		L=[]
		L.append(a)
		return L

	
>>> f(2)
[2]
>>> f(3)
[3]
>>> f(3,4)
>>> print(f(3,4))
None
>>> def f(a,L=NONE):
	if L is NONE:
		L=[]
		L.append(a)
	return L

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    def f(a,L=NONE):
NameError: name 'NONE' is not defined
>>> def f(a,L=None):
	if L is None:
		L=[]
		L.append(a)
	return L

>>> f(3,4)
4
>>> print(f(3,4))
4
>>> type(f(3,4))
<class 'int'>
>>> def f(a,L=None):
	if L is None:
		L=[]
	L.append(a)
	return L

>>> f(3,4)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    f(3,4)
  File "<pyshell#28>", line 4, in f
    L.append(a)
AttributeError: 'int' object has no attribute 'append'
>>> print(f(3,4))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(f(3,4))
  File "<pyshell#28>", line 4, in f
    L.append(a)
AttributeError: 'int' object has no attribute 'append'
>>> f([1,2,5])
[[1, 2, 5]]
>>> 
