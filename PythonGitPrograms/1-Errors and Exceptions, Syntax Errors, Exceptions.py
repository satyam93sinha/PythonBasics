Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True print 'hey'
SyntaxError: invalid syntax
>>> while True print('hey')
SyntaxError: invalid syntax
>>> 18 * (4/0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    18 * (4/0)
ZeroDivisionError: division by zero
>>> '34'+53
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    '34'+53
TypeError: can only concatenate str (not "int") to str
>>> dir(except)
SyntaxError: invalid syntax
>>> dir(exceptions)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dir(exceptions)
NameError: name 'exceptions' is not defined
>>> dir(TypeError)
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'with_traceback']
>>> TypeError.__class__
<class 'type'>
>>> dir(type)
['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
>>> type.__sizeof__
<method '__sizeof__' of 'type' objects>
>>> type.__mro__
(<class 'type'>, <class 'object'>)
>>> print(type.__doc__)
type(object_or_name, bases, dict)
type(object) -> the object's type
type(name, bases, dict) -> a new type
>>> 
