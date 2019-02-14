Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def class_check():
	a = 4
	print('Function, a:', a)
	class inside_func:
		a = 5
		print('Inside func class, a:', a)
		global a
		
SyntaxError: name 'a' is used prior to global declaration
>>> def class_check():
	global a = 4
	print('Function, a:', a)
	class inside_func:
		a = 5
		print('Inside func class, a:', a)
		global a
		
SyntaxError: invalid syntax
>>> def class_check():
	global a
	a = 4
	print('Function, a:', a)
	class inside_func:
		a = 5
		print('Inside func class, a:', a)
		global a
		
SyntaxError: name 'a' is used prior to global declaration
>>> a = 4
>>> def class_check():
	global a
	a = 8
	# changes value of global name a from 4 to 8
	print('Function, a:', a)
	class inside_func:
		a = 5
		print('Inside func class, a:', a)
		global a
		
SyntaxError: name 'a' is used prior to global declaration
>>> def class_check():
	global a
	a = 8
	# changes value of global name a from 4 to 8
	print('Function, a:', a)
	class inside_func:
		b = 5
		print('Inside func class, a:', a)
		global a
		
SyntaxError: name 'a' is used prior to global declaration
>>> def class_check():
	global a
	a = 8
	# changes value of global name a from 4 to 8
	print('Function, a:', a)
	if(a <=  8):
		class inside_func:
			b = 5
			print('Inside func class, a:', b)
			global a
			a = 15print('Class Inside func, a:', a)
			
SyntaxError: invalid syntax
>>> def class_check():
	global a
	a = 8
	# changes value of global name a from 4 to 8
	print('Function, a:', a)
	if(a <=  8):
		class inside_func():
			b = 5
			print('Inside func class, a:', b)
			global a
			a = 15
			print('Class Inside func, a:', a)
		obj = inside_func()

		
>>> 
>>> class_check()
Function, a: 8
Inside func class, a: 5
Class Inside func, a: 15
>>> a
15
>>> def class_check():
	global a
	a = 8
	# changes value of global name a from 4 to 8
	print('Function, a:', a)
	if(a <=  8):
		class inside_func():
			b = 5
			print('Inside func class, a:', b)
			global a
			a = 15
			print('Class Inside func, a:', a)

			
>>> class_check()
Function, a: 8
Inside func class, a: 5
Class Inside func, a: 15
>>> obj = class_check().inside_func().b
Function, a: 8
Inside func class, a: 5
Class Inside func, a: 15
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    obj = class_check().inside_func().b
AttributeError: 'NoneType' object has no attribute 'inside_func'
>>> obj = class_check().inside_func.b
Function, a: 8
Inside func class, a: 5
Class Inside func, a: 15
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    obj = class_check().inside_func.b
AttributeError: 'NoneType' object has no attribute 'inside_func'
>>> def class_check():
	global a
	a = 8
	# changes value of global name a from 4 to 8
	print('Function, a:', a)
	if(a <=  8):
		class inside_func():
			b = 5
			print('Inside func class, a:', b)
			global a
			a = 15
			print('Class Inside func, a:', a)
		obj = inside_func()

		
>>> class_check().obj.b
Function, a: 8
Inside func class, a: 5
Class Inside func, a: 15
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    class_check().obj.b
AttributeError: 'NoneType' object has no attribute 'obj'
>>> # we learn that classes can be anywhere, in a function, in control statement
>>> # within loops. Also, classes will execute on its own without creating an
>>> # object if present inside any of these.
>>> 
