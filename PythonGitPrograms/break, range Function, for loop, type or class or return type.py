Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for n in range(2,10):
	for x in range(2,n):
		if n%x==0:
			print(n,'equals',x,'*',x)
			break
	else:
		print(n,'is a prime number')

		
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 2
7 is a prime number
8 equals 2 * 2
9 equals 3 * 3
>>> range(2,2)
range(2, 2)
>>> range
<class 'range'>
>>> type(range)
<class 'type'>
>>> type(range(2,2))
<class 'range'>
>>> type(list(range(2,2)))
<class 'list'>
>>> list(range(2,2))
[]
>>> list(range(2,3))
[2]
>>> for n in range(2,10):
	for x in range(2,n):
		if n%x==0:
			print(n,'equals',x,'*',n//x)
	else:
		print(n,'is a prime number')

		
2 is a prime number
3 is a prime number
4 equals 2 * 2
4 is a prime number
5 is a prime number
6 equals 2 * 3
6 equals 3 * 2
6 is a prime number
7 is a prime number
8 equals 2 * 4
8 equals 4 * 2
8 is a prime number
9 equals 3 * 3
9 is a prime number
>>> for n in range(2,10):
	for x in range(2,n):
		if n%x==0:
			print(n,'equals',x,'*',n//x)
			break
	else:
		print(n,'is a prime number')

		
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
>>> 
