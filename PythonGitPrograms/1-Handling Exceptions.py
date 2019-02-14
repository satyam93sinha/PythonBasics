Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True:
	try:
		num = int(input("Enter a valid num:"))
		break
	except ValueError:
		print("Sorry, invalid num, try again")

		
Enter a valid num:r
Sorry, invalid num, try again
Enter a valid num:r
Sorry, invalid num, try again
Enter a valid num:e
Sorry, invalid num, try again
Enter a valid num:w
Sorry, invalid num, try again
Enter a valid num:s
Sorry, invalid num, try again
Enter a valid num:3
>>> while True:
	try:
		num = int(input("Enter a valid num:"))
		break
	except ValueError as InvalidNum:
		print("InvalidNUM:Sorry, invalid num, try again")

		
Enter a valid num:
InvalidNUM:Sorry, invalid num, try again
Enter a valid num:
InvalidNUM:Sorry, invalid num, try again
Enter a valid num:6
>>> while True:
	try:
		num = int(input("Enter a valid num:"))
		break
	except ValueError:
		print("InvalidNUM: Sorry, invalid num, try again")

		
Enter a valid num:
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    num = int(input("Enter a valid num:"))
KeyboardInterrupt
>>> # control-c interrupts the program raising KeyboardInterrupt exception
>>> while True:
	try:
		num = int(input("Enter a valid num:"))
		print("Try block in Handling Exception execution finished")
		break
	except ValueError:
		print("InvalidNumber: Sorry, invalid num, try again")

		
Enter a valid num:u
InvalidNumber: Sorry, invalid num, try again
Enter a valid num:8
Try block in Handling Exception execution finished
>>> while True;
SyntaxError: invalid syntax
>>> while True:
	try:
		num = int(input("Enter num:"))
		print("Num exception handled")
		tup = tuple(input("Enter tuple:"))
		print("Tuple exception handled")
		try:
			dic = dict(input("Enter dictionary:"))
			print("Inner try block, dict exception handled")
		except ValueError:
			print("InvalidDictionary: dict exception handled")
	except (RuntimeError, NameError, ZeroDivisionError):
		print("Invalid exceptions")
	except ValueError:
		print("ValueError: Values Mismatch")

		
Enter num:h
ValueError: Values Mismatch
Enter num:8
Num exception handled
Enter tuple:u
Tuple exception handled
Enter dictionary:(3,4)
InvalidDictionary: dict exception handled
Enter num:9
Num exception handled
Enter tuple:(3,4)
Tuple exception handled
Enter dictionary:'3',  '4'
InvalidDictionary: dict exception handled
Enter num:8
Num exception handled
Enter tuple:(3)
Tuple exception handled
Enter dictionary:{}
InvalidDictionary: dict exception handled
Enter num:
Traceback (most recent call last):
  File "<pyshell#30>", line 3, in <module>
    num = int(input("Enter num:"))
KeyboardInterrupt
>>> type({})
<class 'dict'>
>>> dict({})
{}
>>> d = ((3,9),(4,16))
>>> type(d)
<class 'tuple'>
>>> dict(d)
{3: 9, 4: 16}
>>> while True:
	try:
		num = int(input("Enter num:"))
		print("Num exception handled")
		tup = tuple(input("Enter tuple:"))
		print("Tuple exception handled")
		try:
			dic = dict(input("Enter dictionary:"))
			print("Inner try block, dict exception handled")
	except (RuntimeError, NameError, ZeroDivisionError):
		print("Invalid exceptions")
	except ValueError:
		print("ValueError: Values Mismatch")
		
SyntaxError: unexpected unindent
>>> while True:
	try:
		num = int(input("Enter num:"))
		print("Num exception handled")
		tup = tuple(input("Enter tuple:"))
		print("Tuple exception handled")
		try:
			dic = dict(input("Enter dictionary:"))
			print("Inner try block, dict exception handled")
	except (RuntimeError, NameError, ZeroDivisionError):
		print("Invalid exceptions")
	except ValueError:
		print("ValueError: Values Mismatch")
		
SyntaxError: unexpected unindent
>>> while True:
	try:
		num = int(input("enter num:"))
		print("num exception clause entered, handled by handler")
		break
	    try:
		    
SyntaxError: unindent does not match any outer indentation level
>>> while True:
	try:
		num = int(input("enter num:"))
		print("num exception clause entered, handled by handler")
		break
		try:
			dic = dict(input("Enter dict:"))
			print("dict exception handled")
	except ValueError:
		
SyntaxError: unexpected unindent
>>> while True:
	try:
		num = int(input("enter num:"))
		print("num exception clause entered, handled by handler")
		break
		try:
			dic = dict(input("Enter dict:"))
			print("dict exception handled")
			break
	except ValueError:
		
SyntaxError: unexpected unindent
>>> while True:
	try:
		num = int(input("enter num:"))
		print("num exception clause entered, handled by handler")
		break
		try:
			dic = dict(input("Enter dict:"))
			print("dict exception handled")
			break
		except RuntimeError:
			print("Wrong Exception raised")
	except ValueError:
		print("ValueError: Type Misamatch for num")
	except ValueError:
		print("ValueError: Type mismatch for dict")

		
enter num:g
ValueError: Type Misamatch for num
enter num:d
ValueError: Type Misamatch for num
enter num:3
num exception clause entered, handled by handler
>>> while True:
	try:
		num = int(input("enter num:"))
		print("num exception clause entered, handled by handler")
		try:
			dic = dict(input("Enter dict:"))
			print("dict exception handled")
			break
		except RuntimeError:
			print("Wrong Exception raised")
	except ValueError:
		print("ValueError: Type Misamatch for num")
	except ValueError:
		print("ValueError: Type mismatch for dict")

		
enter num:4
num exception clause entered, handled by handler
Enter dict:((3,9), (4,16))
ValueError: Type Misamatch for num
enter num:4
num exception clause entered, handled by handler
Enter dict:dict(3,9)
ValueError: Type Misamatch for num
enter num:
Traceback (most recent call last):
  File "<pyshell#62>", line 3, in <module>
    num = int(input("enter num:"))
KeyboardInterrupt
>>> dict('string')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dict('string')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict('string', 'type change')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict('string', 'type change')
TypeError: dict expected at most 1 arguments, got 2
>>> dict(('string', 'type change'))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(('string', 'type change'))
ValueError: dictionary update sequence element #0 has length 6; 2 is required
>>> dict(('st', 'type change'))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    dict(('st', 'type change'))
ValueError: dictionary update sequence element #1 has length 11; 2 is required
>>> dict(('st','type change'),('s', 'exception'))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(('st','type change'),('s', 'exception'))
TypeError: dict expected at most 1 arguments, got 2
>>> dict([('st','type change'),('s', 'exception')])
{'st': 'type change', 's': 'exception'}
>>> while True:
	try:
		num = int(input("enter num:"))
		print("num exception clause entered, handled by handler")
		try:
			dic = dict(input("Enter dict:"))
			print("dict exception handled")
			break
		except RuntimeError:
			print("Wrong Exception raised")
	except ValueError:
		print("ValueError: Type Misamatch for num, dict")

		
enter num:4
num exception clause entered, handled by handler
Enter dict:([(3, 9), (4, 16)])
ValueError: Type Misamatch for num, dict
enter num:4
num exception clause entered, handled by handler
Enter dict:dict([('s
ValueError: Type Misamatch for num, dict
enter num:4
num exception clause entered, handled by handler
Enter dict:dict([('s', 'a'), ('d', 'e')])
ValueError: Type Misamatch for num, dict
enter num:5
num exception clause entered, handled by handler
Enter dict:{3:9, 4:16}
ValueError: Type Misamatch for num, dict
enter num:
Traceback (most recent call last):
  File "<pyshell#70>", line 3, in <module>
    num = int(input("enter num:"))
KeyboardInterrupt
>>> # string can not be converted to dict type
		  
>>> class
		  
SyntaxError: invalid syntax
>>> class B(Exception):
		  pass
class C(B):
		  
SyntaxError: invalid syntax
>>> class B(Exception):
		  pass
    class C(B):
		  
SyntaxError: unindent does not match any outer indentation level
>>> class B(Exception):
		  pass
		class C(B):
		  
SyntaxError: unindent does not match any outer indentation level
>>> cls()
		  
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    cls()
NameError: name 'cls' is not defined
>>> cls = 
