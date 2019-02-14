Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict_loop_technique = {1:1, 2:4, 3:9}
>>> dict_cube = {x:x**2 for x in range(8)}
>>> dict_cube
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
>>> type(dict_cube)
<class 'dict'>
>>> dict_cube.keys()
dict_keys([0, 1, 2, 3, 4, 5, 6, 7])
>>> dict_cube.__getitems__()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dict_cube.__getitems__()
AttributeError: 'dict' object has no attribute '__getitems__'
>>> dict_cube.__getitem__()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict_cube.__getitem__()
TypeError: __getitem__() takes exactly one argument (0 given)
>>> dict_cube.__getitem__
<built-in method __getitem__ of dict object at 0x03B836F0>
>>> dict_cube.__getitem__(3)
9
>>> for k, v in dict_cube.items():
	print(k,v)

	
0 0
1 1
2 4
3 9
4 16
5 25
6 36
7 49
>>> type(dict_cube.items())
<class 'dict_items'>
>>> for k, v in enumerate(dict_cube):
	print(k,v)

	
0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
>>> <class 'dict_items'>
SyntaxError: invalid syntax
>>> 
>>> 
>>> for k in enumerate(dict_cube):
	print(k)

	
(0, 0)
(1, 1)
(2, 2)
(3, 3)
(4, 4)
(5, 5)
(6, 6)
(7, 7)
>>> for k in enumerate(dict_cube):
	print('key :\t', k)

	
key :	 (0, 0)
key :	 (1, 1)
key :	 (2, 2)
key :	 (3, 3)
key :	 (4, 4)
key :	 (5, 5)
key :	 (6, 6)
key :	 (7, 7)
>>> for k in enumerate(dict_cube):
	print("hEY")

	
hEY
hEY
hEY
hEY
hEY
hEY
hEY
hEY
>>> type(enumerate(dict_cube))
<class 'enumerate'>
>>> enumerate
<class 'enumerate'>
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(enumerate)
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |  
 |  Return an enumerate object.
 |  
 |    iterable
 |      an object supporting iteration
 |  
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |  
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> for k in enumerate(dict_cube, start = 9):
	print(k)

	
(9, 0)
(10, 1)
(11, 2)
(12, 3)
(13, 4)
(14, 5)
(15, 6)
(16, 7)
>>> # enumerate() returns the enumerate object, start is its keyword argument,
>>> dict_cube.__reduce__()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict_cube.__reduce__()
  File "G:\Softwares\Python 3.7.0\lib\copyreg.py", line 65, in _reduce_ex
    raise TypeError("can't pickle %s objects" % base.__name__)
TypeError: can't pickle dict objects
>>> dict_cube.__new__(*args, **kwargs)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict_cube.__new__(*args, **kwargs)
NameError: name 'args' is not defined
>>> enumerate.__getattribute__()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    enumerate.__getattribute__()
TypeError: descriptor '__getattribute__' of 'enumerate' object needs an argument
>>> enumerate.__getattribute__(dict_cube)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    enumerate.__getattribute__(dict_cube)
TypeError: descriptor '__getattribute__' requires a 'enumerate' object but received a 'dict'
>>> help(reversed)
Help on class reversed in module builtins:

class reversed(object)
 |  reversed(sequence, /)
 |  
 |  Return a reverse iterator over the values of the given sequence.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __length_hint__(...)
 |      Private method returning an estimate of len(list(it)).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __setstate__(...)
 |      Set state information for unpickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> 
