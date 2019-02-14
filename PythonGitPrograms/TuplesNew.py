Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tuple
<class 'tuple'>
>>> t = tuple(1,4,3,5)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    t = tuple(1,4,3,5)
TypeError: tuple expected at most 1 arguments, got 4
>>> #We can not type cast multiple arguments into a tuple, it expects just one.
>>> t = tuple((1,2,5))
>>> t
(1, 2, 5)
>>> type(t)
<class 'tuple'>
>>> #Here, we have reduced the multiple arguments to one by putting it together.
>>> tuple_list = tuple([1,3,4])
>>> tuple_list
(1, 3, 4)
>>> type(tuple_list)
<class 'tuple'>
>>> class (tuple_list)
SyntaxError: invalid syntax
>>> #Here, we have type casted a list into tuple storing in tuple_list.
>>> tuple_no_typecast = 1,'simple','tuple','definition',2
>>> type(tuple_no_typecast)
<class 'tuple'>
>>> tuple_no_typecast
(1, 'simple', 'tuple', 'definition', 2)
>>> """We are simply assigning multiple values separated by commas to
    tuple_no_typecast. In python, objects get their data types by their
    definition, thus these sequence data get enclosed into paranthesis,
    forming a tuple"""
'We are simply assigning multiple values separated by commas to\n    tuple_no_typecast. In python, objects get their data types by their\n    definition, thus these sequence data get enclosed into paranthesis,\n    forming a tuple'
>>> a,b = tuple_list
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a,b = tuple_list
ValueError: too many values to unpack (expected 2)
>>> #ValueError bcoz the number of elements in tuple_list to unpack is more than
>>> # the number of variables, objects here in python, declared.
>>> 
