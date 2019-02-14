Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> id(a)
1818835264
>>> id(5)
1818835264
>>> a += 1
>>> id(a)
1818835280
>>> id(5)
1818835264
>>> a = 4
>>> a = a+4
>>> id(a)
1818835312
>>> id(4)
1818835248
>>> # a is name/object of integer data-type/identifier
>>> # use id() to check its memory location in RAM
>>> # firstly, memory location remains same but with performing addition
>>> # operation the result(object of integer type) is stored at different locatn
>>> # a is not an object, its just an identifier, 5 is object of int data-type
>>> # Initially, an object 2 is created and the name a is associated with it,
>>> # when we do a = a+1, a new object 3 is created and now a associates with
>>> # this object. "a is reassigned"
>>> abs(a)
8
>>> a
8
>>> # abs is for absolute value of object passed as an argument.
>>> def outer_func():
	a = 30
	def inner_func()"
	
SyntaxError: EOL while scanning string literal
>>> def outer_func():
	a = 30
	def inner_func():
		a = 20
		print('a =', a)

		
>>> outer_func()
>>> outer_func().inner_func()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    outer_func().inner_func()
AttributeError: 'NoneType' object has no attribute 'inner_func'
>>> def outer_func():
	a = 30
	def inner_func():
		a = 20
		print('Nested local namespace:a =', a)
	inner_func()
	print('Local namespace, local symbol table, outer_func():a =', a)

	
>>> outer_func()
Nested local namespace:a = 20
Local namespace, local symbol table, outer_func():a = 30
>>> a = 10
>>> print('Global namespace: a=', a)
Global namespace: a= 10
>>> # The example is given above in different namespaces, scopes
>>> def outer_func():
	global a
	a = 30
	def inner_func():
		global a
		a = 20
		print('Nested local namespace:a =', a)
	inner_func()
	print('Local namespace, local symbol table, outer_func():a =', a)

	
>>> outer_func()
Nested local namespace:a = 20
Local namespace, local symbol table, outer_func():a = 20
>>> a
20
>>> """Thus, here changes occur to 'a' which is in global namespace bcoz
    we defined global a before defining it in outer_func() and inner_func()"""
"Thus, here changes occur to 'a' which is in global namespace bcoz\n    we defined global a before defining it in outer_func() and inner_func()"
>>> # global a accesses 'a' in global namespace memory and reassigns it in
>>> # current namespace, changing its value.
>>> 
