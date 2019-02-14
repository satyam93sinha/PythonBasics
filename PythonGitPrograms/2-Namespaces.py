Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def outer():
	a = 4
	def inner():
		nonlocal a
		a = 5
		print('Nonlocal a: ',a)
	inner()
	print('Outer() scope var a: ', a)

	
>>> outer()
Nonlocal a:  5
Outer() scope var a:  5
>>> # nonlocal is a keyword referencing objects of enclosing function from
>>> # innermost function.
>>> 
