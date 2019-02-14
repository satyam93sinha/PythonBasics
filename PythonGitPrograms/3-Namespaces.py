Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 3
>>> locals()['a']
3
>>> global()['a']
SyntaxError: invalid syntax
>>> global a
>>> a
3
>>> type(locals())
<class 'dict'>
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 3}
>>> type(global)
SyntaxError: invalid syntax
>>> global()
SyntaxError: invalid syntax
>>> type(global a)
SyntaxError: invalid syntax
>>> noun = 'troubles'
>>> noun2 = 'hound'
>>> print("{a}, {noun} and {noun2} dynamic name resolution".format(**locals()))
3, troubles and hound dynamic name resolution
>>> # unpacking of dictionary, locals() return dictionary, is of <class 'dict'>
>>> # this occurs dynamically, provides value to keys a, noun, noun2 dynamically
>>> def out_outer():
	def outer():
		spam = 'local spam
		
SyntaxError: EOL while scanning string literal
>>> def out_outer():
	def outer():
		spam = 'local spam'
		print('local scope:', spam)
	def non_local():
		nonlocal spam
		
SyntaxError: no binding for nonlocal 'spam' found
>>> def out_outer():
	spam = 'test spam'
	def local_scope():
		spam = 'local spam'
		print('local scope:', spam)
	def non_local():
		nonlocal spam
		spam = 'nonlocal spam'
	def global_scope():
		global spam
		spam = 'global spam'
	local_scope()
	print('local_scope:'spam)
	
SyntaxError: invalid syntax
>>> def out_outer():
	spam = 'test spam'
	def local_scope():
		spam = 'local spam'
		print('local scope:', spam)
	def non_local():
		nonlocal spam
		spam = 'nonlocal spam'
	def global_scope():
		global spam
		spam = 'global spam'
	local_scope()
	print('local_scope:', spam)
	non_local()
	print('non_local scope:', spam)
	print('global_scope:', spam)

	
>>> out_outer()
local scope: local spam
local_scope: test spam
non_local scope: nonlocal spam
global_scope: nonlocal spam
>>> # didn't call global_scope(), this function changed reassigned spam name
>>> # first local_scope() is called, then sequentially as mentioned above
>>> 
