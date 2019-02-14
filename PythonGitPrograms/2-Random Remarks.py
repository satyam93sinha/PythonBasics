Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class A:
	def B(self, i):
		print(i)

		
>>> x = A()
>>> x.B = 5
>>> x.B
5
>>> x.B()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x.B()
TypeError: 'int' object is not callable
>>> x.B(6)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x.B(6)
TypeError: 'int' object is not callable
>>> # Data Attribute B, defined outside scope of Class A but in its namespace
>>> # through instance object x, overrides method attribute B.
>>> # Now, whenever we try to call function object B of class A, we get
>>> # TypeError
>>> A.B(A,8)
8
>>> # thus, function B can only be accessed as function object and never as
>>> # method object, method object gets overriden with data attribute.
>>> A.B
<function A.B at 0x0091C618>
>>> x.B
5
>>> del x.B
>>> x.B
<bound method A.B of <__main__.A object at 0x035BEC90>>
>>> # after deleting the data attribute B, same name of function B in class A,
>>> # we can clearly see that function B is accessible as method object.
>>> # as well as function object both.
>>> x.B(8)
8
>>> # it prints i passed to method attribute/method object B(self, i)
>>> x.B.j = 10
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x.B.j = 10
AttributeError: 'method' object has no attribute 'j'
>>> x.B(8).j = 3
8
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x.B(8).j = 3
AttributeError: 'NoneType' object has no attribute 'j'
>>> # we can't define a data attribute for method object
>>> class A:
	def B(self, i):
		j = 24
		print(i, j)

		
>>> x = A()
>>> x.B.j
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x.B.j
AttributeError: 'function' object has no attribute 'j'
>>> A.B(A, 2).j
2 24
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    A.B(A, 2).j
AttributeError: 'NoneType' object has no attribute 'j'
>>> s = A.B(A, 2)
2 24
>>> s.j
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.j
AttributeError: 'NoneType' object has no attribute 'j'
>>> class A:
	def B(self, i):
		print(i)
		def C(self, j):
			print(j)

			
>>> x = A()
>>> x.B.C
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    x.B.C
AttributeError: 'function' object has no attribute 'C'
>>> x.C
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x.C
AttributeError: 'A' object has no attribute 'C'
>>> class A:
	def B(self, i):
		print(i)
		def C(j):
			print(j)

			
>>> x = A()
>>> x.B(3).C(2)
3
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x.B(3).C(2)
AttributeError: 'NoneType' object has no attribute 'C'
>>> 
