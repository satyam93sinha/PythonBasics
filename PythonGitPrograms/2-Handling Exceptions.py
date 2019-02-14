Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True:
	try:
		number = int(input('Enter a number:'))
		print('try block execution finished')
		break
	finally:
		print("Not a number, try again...")

		
Enter a number:d
Not a number, try again...
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    number = int(input('Enter a number:'))
ValueError: invalid literal for int() with base 10: 'd'
>>> # when the exception isn't handled explicitly through a handler, built-in
>>> # exceptions are triggered, raising exceptions, as here ValueError.
>>> # try must always be followed by an except or finally clause, or both.
>>> 
== RESTART: G:/Softwares/Python 3.7.0/class, handling exceptions script.py ==
B
C
D
>>> 
== RESTART: G:/Softwares/Python 3.7.0/class, handling exceptions script.py ==
B
C
C
>>> 
== RESTART: G:/Softwares/Python 3.7.0/class, handling exceptions script.py ==
B
B
B
>>> import sys
>>> f = open('file1.txt')
>>> s = f.readline()
>>> i = int(s.strip())
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    i = int(s.strip())
ValueError: invalid literal for int() with base 10: 'traditional chinese encoding'
>>> f.encoding
'cp1252'
>>> f.encoding = 'ascii'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    f.encoding = 'ascii'
AttributeError: readonly attribute
>>> print(sys.exc_info()[0])
None
>>> sys.exc_info()
(None, None, None)
>>> try:
	raise Exception("arg0", "arg1")
except Exception as inst_ex:
	print(type(int_ex))
	# the exception instance is inst_ex
	print(inst_ex.args)
	# displays arguments stored in .args of the instance
	print(inst_ex)
	# displays the arguments directly through __str__
	# may be overridden in Exception subclasses
	x, y =  inst_ex.args
	# unpacking a inst_ex.args tuple
	print("x:{0}, y{1}".format(x, y))

	
Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    raise Exception("arg0", "arg1")
Exception: ('arg0', 'arg1')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#50>", line 4, in <module>
    print(type(int_ex))
NameError: name 'int_ex' is not defined
>>> try:
	raise Exception("arg0", "arg1")
except Exception as inst_ex:
	print(type(inst_ex))
	# the exception instance is inst_ex
	print(inst_ex.args)
	# displays arguments stored in .args of the instance
	print(inst_ex)
	# displays the arguments directly through __str__
	# may be overridden in Exception subclasses
	x, y =  inst_ex.args
	# unpacking a inst_ex.args tuple
	print("x:{0}, y{1}".format(x, y))

	
<class 'Exception'>
('arg0', 'arg1')
('arg0', 'arg1')
x:arg0, yarg1
>>> try:
	raise Exception("arg0", "arg1")
except Exception as inst_ex:
	print(type(inst_ex))
	# the exception instance is inst_ex
	print(inst_ex.args)
	# displays arguments stored in .args of the instance
	print(inst_ex)
	# displays the arguments directly through __str__
	# may be overridden in Exception subclasses
	x, y =  inst_ex.args
	# unpacking a inst_ex.args tuple
	print("x:{0}, y:{1}".format(x, y))

	
<class 'Exception'>
('arg0', 'arg1')
('arg0', 'arg1')
x:arg0, y:arg1
>>> while True:
	try:
		n = int(input("Enter number:"))
		raise Exception('check', 'args')
		break
	except Exception as inst_ex:
		print("Exception: {0}".format(inst_ex))
		print(inst_ex)

		
Enter number:5
Exception: ('check', 'args')
('check', 'args')
Enter number:d
Exception: invalid literal for int() with base 10: 'd'
invalid literal for int() with base 10: 'd'
Enter number:
Traceback (most recent call last):
  File "<pyshell#62>", line 3, in <module>
    n = int(input("Enter number:"))
KeyboardInterrupt
>>> # the same continues repeatedly bcoz first exception is raised then we are
>>> # voluntarily raising another exception to test for arguments in exceptions
>>> # Also, inst_ex displays the description of error message above for the
>>> # first exception raised due to ValueError, type mismatch.
>>> 
