Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: G:/Softwares/Python/Instance output check.py ===========
{}
{'name': 'Toyota'}
car class dictionary {'__module__': '__main__', 'wheels': 4, 'name': 'other', '__init__': <function Car.__init__ at 0x0000028FDA1A2EA0>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
>>> d={'aman':'name',
       'john':'name'}
>>> print('name' in d)
False
>>> a=(x**x for x in range(5))
>>> a.__next__()
1
>>> a.__next__()
1
>>> b=list(a)
>>> print(b)
[4, 27, 256]
>>> #__next__ iterates or goes to next iteration for that generator expression
>>> # runs 5 times,two of the values are consumed through __next__  metaproperty
>>> a=(x**x for x in range(5))
>>> print(a.__next__)
<method-wrapper '__next__' of generator object at 0x0000028FDAC7B888>
>>> c=a.__next__
>>> c
<method-wrapper '__next__' of generator object at 0x0000028FDAC7B888>
>>> print(list(c))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(list(c))
TypeError: 'method-wrapper' object is not iterable
>>> print(c)
<method-wrapper '__next__' of generator object at 0x0000028FDAC7B888>
>>> c=a.__next__()
>>> c
1
>>> print(a.__next__())
1
>>> z=(x**x for x in range(5))
>>> z.__next__()
1
>>> z=(x**2 for x in range(5))
>>> z.__next__()
0
>>> z.__next__()
1
>>> x=[2,3]
>>> id(x)
2816874385864
>>> id(x[0])
1870249008
>>> def func():
	x=['abc','def']
	return id(x)

>>> x=['abc','def']
>>> print(id(x)==func())
False
>>> print(id(x[0])==func())
False
>>> print(id(x[0])==func())def func():
	x=['abc','def']
	return id(x)
SyntaxError: invalid syntax
>>> def func():
	x=['abc','def']
	return id(x[0])

>>> print(id(x[0])==func())
True
>>> def func():
	x=['abc','def']
	return id(x)

>>> print(id(x)==func())
False
>>> x=['abc','def']
>>> print(id(x)==func())
False
>>> 
