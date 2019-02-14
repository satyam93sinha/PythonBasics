Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Base:
	def __init__(self):
		self._a = 4
		print(self._a)

		
>>> base = Base()
4
>>> base._a
4
>>> class Child(Base):
	print("Child")

	
Child
>>> child = Child()
4
>>> child._a
4
>>> class Child(Base):
	def __init__(self):
		print("Child constructor")

		
>>> child = Child()
Child constructor
>>> child._a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    child._a
AttributeError: 'Child' object has no attribute '_a'
>>> class Child(Base):
	def __init__(self):
		print("Child constructor")
		super().__init__()

		
>>> child = Child()
Child constructor
4
>>> child._a
4
>>> # name prefixed with an underscore, considered a part of non-public API
>>> # can also be inherited and accessed through subclass' object.
>>> class Base:
	def __init__(self):
		self.__a = 4
		print(self.__a)

		
>>> base = Base()
4
>>> base.__
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    base.__
AttributeError: 'Base' object has no attribute '__'
>>> base.__A
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    base.__A
AttributeError: 'Base' object has no attribute '__A'
>>> base.__a
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    base.__a
AttributeError: 'Base' object has no attribute '__a'
>>> # Python converts __a to _Base__a, it actually textually replaces it.
>>> # Thus, stays inaccessible to objects outside class and are said to be
>>> # private variables with limited support to Name Mangling.
>>> Base.__a
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    Base.__a
AttributeError: type object 'Base' has no attribute '__a'
>>> Base.__init__(Base).__a
4
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Base.__init__(Base).__a
AttributeError: 'NoneType' object has no attribute '__a'
>>> class Base:
	def __init__(self):
		self.__a = 4
		print(self.__a)

		
>>> base.__a
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    base.__a
AttributeError: 'Base' object has no attribute '__a'
>>> # Python converts __a to _Base__a, it actually textually replaces it.
>>> # Thus, stays inaccessible to objects outside class and are said to be
>>> # private variables with limited support to Name Mangling.
>>> base._Base__a
4
>>> # Name Mangling literally means destroying names, here __a is replaced with
>>> # _Base__a thus it is called name mangling.
>>> Base._Base__a
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    Base._Base__a
AttributeError: type object 'Base' has no attribute '_Base__a'
>>> Base.__init__(Base)
4
>>> Base.__init__(Base)._Base__a
4
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    Base.__init__(Base)._Base__a
AttributeError: 'NoneType' object has no attribute '_Base__a'
>>> # it is a constructor so can only be accessed through instance objects
>>> # like in Java.
>>> _internal_name
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    _internal_name
NameError: name '_internal_name' is not defined
>>> 
