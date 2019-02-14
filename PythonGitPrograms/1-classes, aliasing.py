Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Print():
	print("Hello Class!")

	
Hello Class!
>>> p = Print()
>>> p
<__main__.Print object at 0x031DFEF0>
>>> id(Print())
55816784
>>> Print
<class '__main__.Print'>
>>> id(Print)
55780792
>>> id(p)
52297456
>>> # Memory Locations to Print object, already pre-defined by creating a class
>>> # returns a newly created class name
>>> type(Print)
<class 'type'>
>>> type(Print())
<class '__main__.Print'>
>>> # Print is an object so returns "<class 'type'>" whereas Print() is class
>>> # thus returns a class of __main__ (may be constructor)
>>> type(__main__)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(__main__)
NameError: name '__main__' is not defined
>>> object.__main__
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    object.__main__
AttributeError: type object 'object' has no attribute '__main__'
>>> __name__
'__main__'
>>> # the name of the class here is set to '__main__',
>>> # we know main method is important in Java, execution starts from there.
>>> # name of class isn't set to '__main__',
>>> # here __main__ is the interpreter or area where execution starts just like
>>> # other programming languages but here whatever in __main__ gets executed
>>> # if called.
>>> class Print(a):
	print(a)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    class Print(a):
NameError: name 'a' is not defined
>>> p = Print(4)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    p = Print(4)
TypeError: Print() takes no arguments
>>> class Print():
	a = 4
	print(a)

	
4
>>> p = Print().a
>>> p
4
>>> p = 5
>>> Print()
<__main__.Print object at 0x031DFEF0>
>>> Print.a = 5
>>> Print
<class '__main__.Print'>
>>> dir(Print)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a']
>>> Print.a
5
>>> # value of a of class Print() has been changed to 5 from 4.
>>> # through pre-defined object Print of same name as class name.
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
>>> a == b
True
>>> b is a
False
>>> b == a
True
>>> # through '==' equality we check if the elements/data present is same
>>> id(a)
1798952
>>> id(b)
51700200
>>> # as the id are different, memory locations for a and b are different.
>>> # thus a is b and b is a returns false.
>>> b = a
>>> b is a
True
>>> id(a)
1798952
>>> id(b)
1798952
>>> # when reassigned a to b, id of a and b became same so returns true.
>>> # this is called aliasing in other languages, aliasing has no effect on
>>> # immutable objects because they can't be changed
>>> # but as here's a list, we can append values to see the effect
>>> a.append(5)
>>> a
[1, 2, 3, 5]
>>> b
[1, 2, 3, 5]
>>> a is b
True
>>> b is a
True
>>> b.pop
<built-in method pop of list object at 0x001B7328>
>>> b.pop()
5
>>> b
[1, 2, 3]
>>> a
[1, 2, 3]
>>> # any append or pop, remove operation has no change on any of a, b object
>>> # changes to one, alters the other, a good effect of aliasing here.
>>> # this occurs bcoz both the objects are at same location in memory,
>>> # used id() to check their location.
>>> 
