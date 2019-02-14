Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(2,30)
SyntaxError: invalid syntax
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")
		else
		
SyntaxError: invalid syntax
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")
		else:
			
SyntaxError: invalid syntax
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")
		else print(i,"is odd")
		
SyntaxError: invalid syntax
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")
		elif
		
SyntaxError: invalid syntax
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")

		
2 is even
4 is even
6 is even
8 is even
10 is even
12 is even
14 is even
16 is even
18 is even
20 is even
22 is even
24 is even
26 is even
28 is even
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")
	else:
		print(i,"is odd")

	
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
10 is even
11 is odd
12 is even
13 is odd
14 is even
15 is odd
16 is even
17 is odd
18 is even
19 is odd
20 is even
21 is odd
22 is even
23 is odd
24 is even
25 is odd
26 is even
27 is odd
28 is even
29 is odd
>>> for i in range(2,30):
	if(i%2==0):
		list(i)
	else:
		list(i)

		
Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    list(i)
TypeError: 'int' object is not iterable
>>> for i in range(2,30):
	for j in range(2,i):
		if (i%j==0):
			print(i,"equals",j,"*",i//j)
			break;
	else:
		print(i, "is a prime number")

		
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
10 equals 2 * 5
11 is a prime number
12 equals 2 * 6
13 is a prime number
14 equals 2 * 7
15 equals 3 * 5
16 equals 2 * 8
17 is a prime number
18 equals 2 * 9
19 is a prime number
20 equals 2 * 10
21 equals 3 * 7
22 equals 2 * 11
23 is a prime number
24 equals 2 * 12
25 equals 5 * 5
26 equals 2 * 13
27 equals 3 * 9
28 equals 2 * 14
29 is a prime number
>>> 
================= RESTART: G:/ProgramsPython/PrimeNumber.py =================
185 equals 5 * 37
186 equals 2 * 93
187 equals 11 * 17
188 equals 2 * 94
189 equals 3 * 63
190 equals 2 * 95
191 is a prime number
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")
		continue
		print(i,"is odd")

		
2 is even
4 is even
6 is even
8 is even
10 is even
12 is even
14 is even
16 is even
18 is even
20 is even
22 is even
24 is even
26 is even
28 is even
>>> for i in range(2,30):
	if(i%2==0):
		print(i,"is even")
		continue
	print(i,"is odd")

	
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
10 is even
11 is odd
12 is even
13 is odd
14 is even
15 is odd
16 is even
17 is odd
18 is even
19 is odd
20 is even
21 is odd
22 is even
23 is odd
24 is even
25 is odd
26 is even
27 is odd
28 is even
29 is odd
>>> while true:
	pass

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    while true:
NameError: name 'true' is not defined
>>> while True:
	pass

Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    pass
KeyboardInterrupt
>>> 
