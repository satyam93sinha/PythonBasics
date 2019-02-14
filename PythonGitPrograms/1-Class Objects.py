Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyClass:
	"""Attribute reference
        accesses, changes, deletes attribute of class"""
	i = 56
	print('i in MyClass:{}'.format(i))
	def MyClass_func(self):
		return 'MyClass_func'

	
i in MyClass:56
>>> MyClass.MyClass_func
<function MyClass.MyClass_func at 0x02F0C618>
>>> MyClass.MyClass_func()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    MyClass.MyClass_func()
TypeError: MyClass_func() missing 1 required positional argument: 'self'
>>> obj = MyClass()
>>> obj.i
56
>>> obj.MyClass_func
<bound method MyClass.MyClass_func of <__main__.MyClass object at 0x0366DC50>>
>>> obj
<__main__.MyClass object at 0x0366DC50>
>>> class MyClass:
	"""Attribute reference
        accesses, changes, deletes attribute of class"""
	i = 56
	print('i in MyClass:{}'.format(i))
	def MyClass_func():
		return 'MyClass_func'

	
i in MyClass:56
>>> MyClass.MyClass_func()
'MyClass_func'
>>> class MyClass:
	"""Attribute reference
        accesses, changes, deletes attribute of class"""
	i = 56
	print('i in MyClass:{}'.format(i))
	def MyClass_func(self):
		return 'MyClass_func'

	
i in MyClass:56
>>> MyClass.MyClass_func(MyClass)
'MyClass_func'
>>> # accessing the valid attribute references of MyClass.
>>> 
