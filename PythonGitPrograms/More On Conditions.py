Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [2,3] is list
False
>>> [2,3] in list
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    [2,3] in list
TypeError: argument of type 'type' is not iterable
>>> # we can't iterate over any argument of type 'type' or class.
>>> # Iteration can only be done on sequences, iterable objects, type isn't that
>>> # type isn't an iterable object.
>>> a_list = [2,3]
>>> type(a_list)
<class 'list'>
>>> a_list is list
False
>>> a_list in list
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a_list in list
TypeError: argument of type 'type' is not iterable
>>> a_list in type(list)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a_list in type(list)
TypeError: argument of type 'type' is not iterable
>>> a_list is not list
True
>>> #a_list is not a list rather a subset of list type.
>>> a, b, c = 3, 2, 3
>>> while(a<b==c):
	print(a,b,c)
	break

>>> a<b==c
False
>>> b<a==c
True
>>> a<b==False
False
>>> a<b
False
>>> a==c
True
>>> b = 4
>>> a<b==c
False
>>> a<b && b==c
SyntaxError: invalid syntax
>>> a<b and b==c
False
>>> #same occurs when we test for a<b==c, so result we see is False.
>>> b>a==c
True
>>> 0 == 0.0
True
>>> 
