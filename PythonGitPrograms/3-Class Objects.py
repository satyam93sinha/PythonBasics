Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyClass:
	def __init__(self, i):
		self.i = i
		i = 5
		print("self.i:{0}, i:{1}, id(self.i):{2}, id(i):{3}"
		      .format(self.i, i, id(self.i), id(i)))
	def simple_functn(i)
	
SyntaxError: invalid syntax
>>> class MyClass:
	def __init__(self, i):
		self.i = i
		i = 5
		print("self.i:{0}, i:{1}, id(self.i):{2}, id(i):{3}"
		      .format(self.i, i, id(self.i), id(i)))
	def simple_functn(i):
		print("simple_function:{}, id(i):{}".format(i, id(i)))

		
>>> obj = MyClass(15)
self.i:15, i:5, id(self.i):1807403360, id(i):1807403200
>>> # see for id(self.i) and id(i) both are different so located at
>>> # different memory locations.
>>> obj.simple_functn
<bound method MyClass.simple_functn of <__main__.MyClass object at 0x0406DDB0>>
>>> obj.simple_functn(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    obj.simple_functn(2)
TypeError: simple_functn() takes 1 positional argument but 2 were given
>>> # requires 1 positional argument, but one was given while creating instance
>>> # of class, thus, that is taken as argument for simple_functn(i)
>>> # here MyClass(15), simple_functn(i) 15 is taken as i.
>>> MyClass.simple_functn(8)
simple_function:8, id(i):1807403248
>>> # i in simple_functn is at different location than those in __init__
>>> class MyClass_2:
	def undefined_var(j):
		print("undefined_var, defined later:{}".format(j))

		
>>> MyClass_2.j = 2
>>> for i in range(5):
	j += i

	
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    j += i
NameError: name 'j' is not defined
>>> for i in range(5):
	MyClass_2.j += i

	
>>> MyClass_2.undefined_var()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    MyClass_2.undefined_var()
TypeError: undefined_var() missing 1 required positional argument: 'j'
>>> MyClass_2.undefined_var(MyClass_2.j)
undefined_var, defined later:12
>>> class MyClass_2:
	def undefined_var(j):
		print("undefined_var, defined later:{}".format(j))

		
>>> x = MyClass_2()
>>> x.j = 3
>>> x.j *= 3
>>> x.j
9
>>> x.undefined_var(x.j)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x.undefined_var(x.j)
TypeError: undefined_var() takes 1 positional argument but 2 were given
>>> x.undefined_var()
undefined_var, defined later:<__main__.MyClass_2 object at 0x011F4530>
>>> MyClass_2.undefined_var(x.j)
undefined_var, defined later:9
>>> 
