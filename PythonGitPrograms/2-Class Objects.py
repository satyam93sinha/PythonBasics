Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyClass:
	def __init__(self, i):
		i = 5
		print('i:'.format(i))

		
>>> obj = MyClass()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    obj = MyClass()
TypeError: __init__() missing 1 required positional argument: 'i'
>>> # Required positional arg is i
>>> obj = MyClass(10)
i:
>>> class MyClass:
	def __init__(self, i):
		i = 5
		print('i:{}'.format(i))

		
>>> obj = MyClass(10)
i:5
>>> # __init__(self, i) initializes i to 5 at each class instance
>>> # because whenever class instance is created i is reassigned 5, printing 5
>>> class MyClass:
	def __init__(self, i):
		i = 5
		print('i:{}'.format(i))
	def simple_func(i):
		print('simple_func:', i)
	simple_func(i)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    class MyClass:
  File "<pyshell#17>", line 7, in MyClass
    simple_func(i)
NameError: name 'i' is not defined
>>> class MyClass:
	j = 3
	print('j:{}'.format(j))
	i = 12
	print('i in MyClass nonlocal namespace:{}'.format(i))
	def __init__(self, i):
		i = 5
		print('i:{}'.format(i))
	def simple_func(i):
		print('simple_func:', i)
		print('simple_func:', j)
	def function_2(self):
		print('function_2:{}'.format(i))
	simple_func(i)
	simple_func(j)

	
j:3
i in MyClass nonlocal namespace:12
simple_func: 12
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    class MyClass:
  File "<pyshell#22>", line 14, in MyClass
    simple_func(i)
  File "<pyshell#22>", line 11, in simple_func
    print('simple_func:', j)
NameError: name 'j' is not defined
>>> class MyClass:
	j = 3
	print('j:{}'.format(j))
	i = 12
	print('i in MyClass nonlocal namespace:{}'.format(i))
	def __init__(self, i):
		i = 5
		print('i:{}'.format(i))
	def simple_func(i):
		print('simple_func:', i)
		#print('simple_func:', j)
	def function_2(self):
		print('function_2:{}'.format(i))
	simple_func(i)
	#simple_func(j)

	
j:3
i in MyClass nonlocal namespace:12
simple_func: 12
>>> obj = MyClass(5)
i:5
>>> # when an object is created/instance is created __init__ is called
>>> obj.simple_func(5)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    obj.simple_func(5)
TypeError: simple_func() takes 1 positional argument but 2 were given
>>> obj.simple_func()
simple_func: <__main__.MyClass object at 0x039B8330>
>>> obj.simple_func
<bound method MyClass.simple_func of <__main__.MyClass object at 0x039B8330>>
>>> obj.simple_func().i
simple_func: <__main__.MyClass object at 0x039B8330>
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    obj.simple_func().i
AttributeError: 'NoneType' object has no attribute 'i'
>>> obj
<__main__.MyClass object at 0x039B8330>
>>> obj.function_2
<bound method MyClass.function_2 of <__main__.MyClass object at 0x039B8330>>
>>> obj.function_2(obj)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    obj.function_2(obj)
TypeError: function_2() takes 1 positional argument but 2 were given
>>> class MyClass:
	j = 3
	print('j:{}'.format(j))
	i = 12
	print('i in MyClass nonlocal namespace:{}'.format(i))
	def __init__(self, i):
		i = 5
		print('i:{}, self.i:{}'.format(i, self.i))
	def simple_func(i):
		print('simple_func:', i)
		#print('simple_func:', j)
	def function_2(self):
		print('function_2:{}'.format(i))
	simple_func(i)
	#simple_func(j)
	obj = MyClass(14)

	
j:3
i in MyClass nonlocal namespace:12
simple_func: 12
i:5
>>> self.i
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    self.i
NameError: name 'self' is not defined
>>> obj.function_2()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    obj.function_2()
  File "<pyshell#24>", line 13, in function_2
    print('function_2:{}'.format(i))
NameError: name 'i' is not defined
>>> obj.function_2(MyClass)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    obj.function_2(MyClass)
TypeError: function_2() takes 1 positional argument but 2 were given
>>> class MyClass:
	j = 3
	print('j:{}'.format(j))
	i = 12
	print('i in MyClass nonlocal namespace:{}'.format(i))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{}, self.i:{}'.format(i, self.i))
	def simple_func(i):
		print('simple_func:', i)
		#print('simple_func:', j)
	def function_2(self):
		print('function_2:{}'.format(i))
	simple_func(i)
	#simple_func(j)
	obj = MyClass(14)

	
j:3
i in MyClass nonlocal namespace:12
simple_func: 12
i:5, self.i:12
>>> class MyClass:
	j = 3
	print('j:{}'.format(j))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{}, self.i:{}'.format(i, self.i))
	def simple_func(i):
		print('simple_func:', i)
		#print('simple_func:', j)
	def function_2(self):
		print('function_2:{}'.format(i))
	simple_func(i)
	#simple_func(j)
	obj = MyClass(14)

	
j:3
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    class MyClass:
  File "<pyshell#43>", line 13, in MyClass
    simple_func(i)
NameError: name 'i' is not defined
>>> class MyClass:
	j = 3
	print('j:{}'.format(j))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{}, self.i:{}'.format(i, self.i))
	def simple_func(i):
		print('simple_func:', i)
		#print('simple_func:', j)
	def function_2(self):
		print('function_2:{}'.format(i))
	obj = MyClass(14)

	
j:3
i:5, self.i:14
>>> obj = MyClass
>>> obj.function_2(MyClass)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    obj.function_2(MyClass)
  File "<pyshell#45>", line 12, in function_2
    print('function_2:{}'.format(i))
NameError: name 'i' is not defined
>>> obj.function_2(MyClass(1))
i:5, self.i:1
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    obj.function_2(MyClass(1))
  File "<pyshell#45>", line 12, in function_2
    print('function_2:{}'.format(i))
NameError: name 'i' is not defined
>>> obj.simple_func()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    obj.simple_func()
TypeError: simple_func() missing 1 required positional argument: 'i'
>>> obj.simple_func(8)
simple_func: 8
>>> objec = MyClass(15)
i:5, self.i:15
>>> # __init__(self, i) executed, class instance created
>>> objec.simple_func()
simple_func: <__main__.MyClass object at 0x039B8830>
>>> objec.i
15
>>> objec.__init__.i
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    objec.__init__.i
AttributeError: 'function' object has no attribute 'i'
>>> id(objec.i)
1807403360
>>> id(j)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    id(j)
NameError: name 'j' is not defined
>>> id(obj.j)
1807403168
>>> id(obj.i)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    id(obj.i)
AttributeError: type object 'MyClass' has no attribute 'i'
>>> id(obj.__init__(2).i)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    id(obj.__init__(2).i)
TypeError: __init__() missing 1 required positional argument: 'i'
>>> id(obj.__init__(obj, 2).i)
i:5, self.i:2
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    id(obj.__init__(obj, 2).i)
AttributeError: 'NoneType' object has no attribute 'i'
>>> class MyClass:
	j = 3
	id(j)
	print('j:{}'.format(j))
	def __init__(self, i):
		self.i = i
		id(self.i)
		i = 5
		id(i)
		print('i:{}, self.i:{}'.format(i, self.i))
	def simple_func(i):
		print('simple_func:', i, id(i))
	obj = MyClass(14)

	
j:3
i:5, self.i:14
>>> class MyClass:
	j = 3
	print('j:{}, id(j):{}'.format(j, id(j)))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{}, id(i):{}, self.i:{}, id(self.i):{}'.format(i,
									(id(i),
									 self.i,
									 id(self.i))))
		def simple_func(i):
		print('simple_func:', i, id(i))
	obj = MyClass(14)
	
SyntaxError: expected an indented block
>>> class MyClass:
	j = 3
	print('j:{}, id(j):{}'.format(j, id(j)))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{}, id(i):{}, self.i:{}, id(self.i):{}'.format(i,
									(id(i),
									 self.i,
									 id(self.i))))
	def simple_func(i):
		print('simple_func:', i, id(i))
	obj = MyClass(14)

	
j:3, id(j):1807403168
i:5, self.i:14
>>> class MyClass:
	j = 3
	print('j:{}, id(j):{}'.format(j, id(j)))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{}, id(i):{}, self.i:{}, id(self.i):{}'
		      .format(i, id(i), self.i, id(self.i))))
	def simple_func(i):
		print('simple_func:', i, id(i))
	obj = MyClass(14)
	
SyntaxError: invalid syntax
>>> class MyClass:
	j = 3
	print('j:{}, id(j):{}'.format(j, id(j)))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{}, id(i):{}, self.i:{}, id(self.i):{}'
		      .format(i, id(i), self.i, id(self.i)))
	def simple_func(i):
		print('simple_func:', i, id(i))
	obj = MyClass(14)

	
j:3, id(j):1807403168
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    class MyClass:
  File "<pyshell#69>", line 11, in MyClass
    obj = MyClass(14)
  File "<pyshell#66>", line 10, in __init__
    id(self.i))))
IndexError: tuple index out of range
>>> class MyClass:
	j = 3
	print('j:{}, id(j):{}'.format(j, id(j)))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{0}, id(i):{1}, self.i:{2}, id(self.i):{3}'
		      .format(i, id(i), self.i, id(self.i)))
	def simple_func(i):
		print('simple_func:', i, id(i))
	obj = MyClass(14)

	
j:3, id(j):1807403168
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    class MyClass:
  File "<pyshell#71>", line 11, in MyClass
    obj = MyClass(14)
  File "<pyshell#66>", line 10, in __init__
    id(self.i))))
IndexError: tuple index out of range
>>> class MyClass:
	j = 3
	print('j:{}, id(j):{}'.format(j, id(j)))
	def __init__(self, i):
		self.i = i
		i = 5
		print('i:{0}, id(i):{1}, self.i:{2}, id(self.i):{3}'
		      .format(i, id(i), self.i, id(self.i)))
	def simple_func(i):
		print('simple_func:{0}, id(i):{}'.format(i, id(i)))
	obj = MyClass(14)

	
j:3, id(j):1807403168
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    class MyClass:
  File "<pyshell#73>", line 11, in MyClass
    obj = MyClass(14)
  File "<pyshell#66>", line 10, in __init__
    id(self.i))))
IndexError: tuple index out of range
>>> 
