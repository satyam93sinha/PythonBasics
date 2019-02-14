Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def unpacking_dict(string,integer,double):
	"""A function to show unpacking of dictionary"""
	print(string,'\n',integer,'\n',double)

	
>>> dic={string:'Hey',integer:50,double:65.3}
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dic={string:'Hey',integer:50,double:65.3}
NameError: name 'string' is not defined
>>> dic={'string':'Hey','integer':50,'double':65.3}
>>> unpacking_dict(dic)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    unpacking_dict(dic)
TypeError: unpacking_dict() missing 2 required positional arguments: 'integer' and 'double'
>>> unpacking_dict(dic,2,4.5)
{'string': 'Hey', 'integer': 50, 'double': 65.3} 
 2 
 4.5
>>> unpacking_dict(**dic)
Hey 
 50 
 65.3
>>> def unpacking_dict(string,integer,double):
	"""A function to show unpacking of dictionary"""
	print(string,integer,double)

	
>>> unpacking_dict(**dic)
Hey 50 65.3
>>> a=6
>>> a
6
>>> type(dic('double':65.3))
SyntaxError: invalid syntax
>>> lambda a,b:a+b
<function <lambda> at 0x00000220973961E0>
>>> a
6
>>> b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> lambda
SyntaxError: invalid syntax
>>> def sum():
	return lambda a,b:a+b

>>> sum()
<function sum.<locals>.<lambda> at 0x000002209739B7B8>
>>> def sum():
	return lambda a=int(input("Enter num1")),b=int(input("Enter num2")):a+b

>>> sum
<function sum at 0x000002209739BD08>
>>> sum()
Enter num156
Enter num2100
<function sum.<locals>.<lambda> at 0x00000220973961E0>
>>> def sum():
	print(lambda a=int(input("Enter num1")),b=int(input("Enter num2")):a+b)

	
>>> sum()
Enter num15
Enter num29
<function sum.<locals>.<lambda> at 0x000002209739BD08>
>>> def sum():
	a=int(input("enter a"))
	b=int(input("enter b"))
	print(lambda c:a+b)

	
>>> sum()
enter a3
enter b4
<function sum.<locals>.<lambda> at 0x000002209739B7B8>
>>> def sum():
	a=int(input("enter a"))
	b=int(input("enter b"))
	print(lambda c:a+b)
	print(c)

	
>>> sum()
enter a23
enter b3
<function sum.<locals>.<lambda> at 0x000002209739B840>
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sum()
  File "<pyshell#36>", line 5, in sum
    print(c)
NameError: name 'c' is not defined
>>> def sum():
	a=int(input("enter a"))
	b=int(input("enter b"))
	return (lambda c:a+b)

>>> sum()
enter a3
enter b3
<function sum.<locals>.<lambda> at 0x000002209739B7B8>
>>> 
