Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: G:/ProgramsPython/1-Private Variables.py =============
>>> mapp = Mapping()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    mapp = Mapping()
TypeError: __init__() missing 1 required positional argument: 'iterable'
>>> mapp = Mapping([1,2,3])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    mapp = Mapping([1,2,3])
  File "G:/ProgramsPython/1-Private Variables.py", line 4, in __init__
    self.__update(iterable)
AttributeError: 'Mapping' object has no attribute '_Mapping__update'
>>> 
============= RESTART: G:/ProgramsPython/1-Private Variables.py =============
>>> mapp = Mapping([1,2,3])
>>> mapp.item_list)(
	
SyntaxError: invalid syntax
>>> mapp.item_list()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mapp.item_list()
TypeError: 'list' object is not callable
>>> mapp.item_list
[1, 2, 3]
>>> # now when we added __update = update, converts it to _Mapping__update
>>> # = update, thus calling update function object of the same class
>>> # this is name convention to provide support to name mangling
>>> 
============= RESTART: G:/ProgramsPython/1-Private Variables.py =============
>>> mapp = Mapping([1,2,3])
>>> mapp.item_list
[1, 2, 3]
>>> Ch = Child({1:1, 2:4})
>>> Ch.item_list
[1, 2]
>>> 
============= RESTART: G:/ProgramsPython/1-Private Variables.py =============
>>> Ch = Child({1:1, 2:4})
>>> Ch.item_list
[1, 2]
>>> # it clearly shows __update of Mapping is being invoked
>>> Ch.update()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Ch.update()
TypeError: update() missing 1 required positional argument: 'diction'
>>> Ch.update({1:1, 2:4})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Ch.update({1:1, 2:4})
  File "G:/ProgramsPython/1-Private Variables.py", line 13, in update
    for keys, values in zip(diction):
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============= RESTART: G:/ProgramsPython/1-Private Variables.py =============
>>> Ch = Child({1:1, 2:4})
>>> Ch.item_list
[1, 2]
>>> Ch.update({1:1, 2:4})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Ch.update({1:1, 2:4})
  File "G:/ProgramsPython/1-Private Variables.py", line 14, in update
    self.item_list.append(i)
NameError: name 'i' is not defined
>>> 
============= RESTART: G:/ProgramsPython/1-Private Variables.py =============
>>> Ch = Child({1:1, 2:4})
>>> Ch.item_list
[1, 2]
>>> Ch.update({1:1, 2:4})
>>> Ch.item_list
[1, 2, {1: 1}, {2: 4}]
>>> #  now it has been appended.
