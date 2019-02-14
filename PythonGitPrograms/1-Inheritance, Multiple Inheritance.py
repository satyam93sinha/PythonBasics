Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class BaseClass:
	def base_function(self):
		return 'Base Function'

	
>>> class DerivedClass(BaseClass):
	def base_function(self):
		return 'Derived Function'

	
>>> child = DerivedClass()
>>> child.base_function
<bound method DerivedClass.base_function of <__main__.DerivedClass object at 0x043D1250>>
>>> child.base_function()
'Derived Function'
>>> # overrides base_function(self) of BaseClass
>>> BaseClass.base_function(self)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    BaseClass.base_function(self)
NameError: name 'self' is not defined
>>> BaseClass.base_function(BaseClass)
'Base Function'
>>> # an object of BaseClass would help us access BaseClass attributes.
>>> class BaseClass:
	def base_function(self):
		base_1()
		return 'Base Function'
	def base_1():
		return ('base_1')

	
>>> base = BaseClass()
>>> base.base_function()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    base.base_function()
  File "<pyshell#18>", line 3, in base_function
    base_1()
NameError: name 'base_1' is not defined
>>> # as expected, we can not access a function before it is defined.
>>> class BaseClass:
	def base_1():
		return ('base_1')
	def base_function(self):
		base_1()
		return 'Base Function'

	
>>> base = BaseClass()
>>> base.base_function()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    base.base_function()
  File "<pyshell#23>", line 5, in base_function
    base_1()
NameError: name 'base_1' is not defined
>>> # scope issue
>>> class BaseClass:
	def base_1():
		return ('base_1')
	def base_function(self):
		BaseClass.base_1()
		return 'Base Function'

	
>>> base = BaseClass()
>>> base = BaseClass()
>>> base.base_function()
'Base Function'
>>> BaseClass.base_1()
'base_1'
>>> class BaseClass:
	def base_1():
		return ('base_1')
	def base_function(self):
		BaseClass.base_1()
		return ('Base Function', BaseClass.base_1())

	
>>> base = BaseClass()
>>> base.base_function()
('Base Function', 'base_1')
>>> class BaseClass:
	def base_1():
		return ('base_1')
	def base_function(self):
		BaseClass.base_1()
		print('Base Function')

		
>>> base = BaseClass()
>>> base.base_function()
Base Function
>>> class BaseClass:
	def base_1():
		return ('base_1')
	def base_function(self):
		print(BaseClass.base_1())
		print('Base Function')

		
>>> base = BaseClass()
>>> base.base_function()
base_1
Base Function
>>> # issue was we weren't printing it thus it compiled but displayed nothing
>>> class DerivedClass(BaseClass):
	def derived_1():
		return('derived_1')
	def base_function(self):
		print('Derived Function')

		
>>> class BaseClass:
	def base_1():
		return ('base_1')
	def base_function(self):
		print(BaseClass.base_1())
		print('Base Function')
	base_1()

	
>>> base = BaseClass()
>>> base
<__main__.BaseClass object at 0x043E9570>
>>> print(base)
<__main__.BaseClass object at 0x043E9570>
>>> class BaseClass:
	def base_1():
		return ('base_1')
	def base_function(self):
		print(BaseClass.base_1())
		print('Base Function')
	print(base_1())

	
base_1
>>> class DerivedClass(BaseClass):
	def base_1():
		return('derived_1')
	def base_function(self):
		print('Derived Function')

		
>>> child = DerivedClass()
>>> child
<__main__.DerivedClass object at 0x03E5BE50>
>>> child.base_function()
Derived Function
>>> # is simply overriding base_function() of BaseClass by DerivedClass
>>> class BaseClass:
	def base_function(self):
		print(BaseClass.base_1())
		print('Base Function')
		def base_1():
		    return ('base_1')
		base_1()

		
>>> BaseClass.base_function(BaseClass)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    BaseClass.base_function(BaseClass)
  File "<pyshell#69>", line 3, in base_function
    print(BaseClass.base_1())
AttributeError: type object 'BaseClass' has no attribute 'base_1'
>>> class BaseClass:
	def base_function(self):
		print('Base Function')
		def base_1():
		    return ('base_1')
		base_1()

		
>>> BaseClass.base_function(BaseClass)
Base Function
>>> class BaseClass:
	def base_function(self):
		print('Base Function')
		def base_1():
		    return ('base_1')
		print(base_1())

		
>>> BaseClass.base_function(BaseClass)
Base Function
base_1
>>> # we were calling base_1() but the return statement was only getting
>>> # stored as an object, displaying nothing, thus using print statement.
>>> class DerivedClass(BaseClass):
	def base_function(self):
		print('Derived Function')
		def derived_function(self):
			print('Derived internal function')
		derived_function(DerivedClass)

		
>>> child = DerivedClass()
>>> child.base_function()
Derived Function
Derived internal function
>>> # overrides BaseClass method base_function() so base_1() present within
>>> # is not accessed. This happens because overriding doesn't let
>>> # child (instance object) overrides BaseClass' method with same name
>>> issubclass(DerivedClass, BaseClass)
True
>>> isinstance(base, DerivedClass)
False
>>> base = BaseClass()
>>> base.base_function()
Base Function
base_1
>>> class Base1:
	def base_1(self):
		print('Base1')

		
>>> class Base2:
	def base_2(self):
		print('Base2')

		
>>> class Derived(Base1, Base2):
	def base_1(self):
		print('Child1')

		
>>> child = Derived()
>>> child.base_1()
Child1
>>> child.base()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    child.base()
AttributeError: 'Derived' object has no attribute 'base'
>>> child.base_2()
Base2
>>> class Base1:
	def base_2(self):
		print('Base1')

		
>>> class Derived(Base1, Base2):
	pass

>>> child = Derived()
>>> child.base_2()
Base1
>>> child.base_2()
Base1
>>> child.base_2()
Base1
>>> # it will always be Base1, first Derived inherits Base1, so searches for
>>> # method object in Base1 class.
>>> 
