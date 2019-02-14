Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> range(2,2)
range(2, 2)
>>> list(range(2,2))
[]
>>> range.response(3,3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    range.response(3,3)
AttributeError: type object 'range' has no attribute 'response'
>>> range.append(3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    range.append(3)
AttributeError: type object 'range' has no attribute 'append'
>>> for n in range(2,10):
	for x in range(2,n):
		print(n,x)

		
3 2
4 2
4 3
5 2
5 3
5 4
6 2
6 3
6 4
6 5
7 2
7 3
7 4
7 5
7 6
8 2
8 3
8 4
8 5
8 6
8 7
9 2
9 3
9 4
9 5
9 6
9 7
9 8
>>> list(range(2,10))
[2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in range(2,10):
	print(i)

	
2
3
4
5
6
7
8
9
>>> for n in range(2,10):
	for x in range(2,n):
		if (n%x == 0):
			print("Not a prime number:\t",n)
			break
	else:
		# when if condition doesn't evaluate to true, loop falls
		# through to else clause.
		print(n, 'is prime number')

		
2 is prime number
3 is prime number
Not a prime number:	 4
5 is prime number
Not a prime number:	 6
7 is prime number
Not a prime number:	 8
Not a prime number:	 9
>>> clr
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> cl
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    cl
NameError: name 'cl' is not defined
s
>>> cls
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> for i in range(5,20):
	if i%2==0:
		print('Even number:\t',i)
		continue
	print('Odd number:\t',i)

	
Odd number:	 5
Even number:	 6
Odd number:	 7
Even number:	 8
Odd number:	 9
Even number:	 10
Odd number:	 11
Even number:	 12
Odd number:	 13
Even number:	 14
Odd number:	 15
Even number:	 16
Odd number:	 17
Even number:	 18
Odd number:	 19
>>> for i in range(5,20):
	if i%2==0:
		print('Even number:\t',i)
		continue
	print('Odd number:\t',i)
	pass

Odd number:	 5
Even number:	 6
Odd number:	 7
Even number:	 8
Odd number:	 9
Even number:	 10
Odd number:	 11
Even number:	 12
Odd number:	 13
Even number:	 14
Odd number:	 15
Even number:	 16
Odd number:	 17
Even number:	 18
Odd number:	 19
>>> 
>>> pass
>>> while True:
	pass

Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    pass
KeyboardInterrupt
>>> pass
>>> 
