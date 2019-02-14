Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(self, x, y):
	return(x, y, x+y)

>>> class A:
	ad = add
	ad_1 = add(5, 3)
	def subtract(self, x, y):
		return(x, y, x-y)

	
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    class A:
  File "<pyshell#8>", line 3, in A
    ad_1 = add(5, 3)
TypeError: add() missing 1 required positional argument: 'y'
>>> class A:
	ad = add
	ad_1 = add(A, 5, 3)
	def subtract(self, x, y):
		return(x, y, x-y)

	
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    class A:
  File "<pyshell#10>", line 3, in A
    ad_1 = add(A, 5, 3)
NameError: name 'A' is not defined
>>> # we learn that until class is executed, its object isn't created
>>> # thus, we can't pass self argument to add() calling as function object
>>> class A:
	ad = add
	def subtract(self, x, y):
		return(x, y, x-y)

	
>>> A_obj = A()
>>> A_obj.ad(5,3)
(5, 3, 8)
>>> A_obj.subtract(8, 3)
(8, 3, 5)
>>> # ad is function object, a class attribute, accessed by instance of class
>>> # defines a method for instances of that class
>>> A.ad(5,4)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    A.ad(5,4)
TypeError: add() missing 1 required positional argument: 'y'
>>> # self here enables class attributes to be accessed through instance objects
>>> # bcoz instance objects are parameterless objects that would add to
>>> # one parameter, self of respective classes.
>>> 
