Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fun_override(self):
	return ("fun_override returned")

>>> class MyClass_3:
	f = fun_override
	def fun_override(self)
	
SyntaxError: invalid syntax
>>> class MyClass_3:
	f = fun_override
	def fun_override(self):
		return("MyClass_3 fun_override returned")

	
>>> MyClass_3.fun_override(MyClass_3)
'MyClass_3 fun_override returned'
>>> MyClass_3.f
<function fun_override at 0x03828540>
>>> MyClass_3.f(MyClass_3)
'fun_override returned'
>>> fun_override(MyClass_3)
'fun_override returned'
>>> fun_override(fun_override)
'fun_override returned'
>>> fun_override(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    fun_override(a)
NameError: name 'a' is not defined
>>> # fun_override(self) takes class object, i.e, self or function name itself.
>>> 
