Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Fibonacci series:")
a=0
b=1
n=1
temp=0
print(a,"\n",b)
while(n<20):
    temp=b
    b=a+b
    print(b)
    a=temp
    n++
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> print("Fibonacci series:")
Fibonacci series:
>>> a=0,b=1,n=1,temp=0
SyntaxError: can't assign to literal
>>> a=0
>>> b=1
>>> n=1
>>> tem=0
>>> print(a,b)
0 1
>>> while(n<20):
	tem=b
	b=a+b
	print(b)
	a=tem
	n=n+1

	
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
>>> print(a,"\n",b)
4181 
 6765
>>> 
================== RESTART: G:/ProgramsPython/Fibonacci.py ==================
Fibonacci series:
0 
 1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
>>> 
================== RESTART: G:/ProgramsPython/Fibonacci.py ==================
Fibonacci series:
0 
 1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
>>> 
================== RESTART: G:/ProgramsPython/Fibonacci.py ==================
Fibonacci series:
0 
 1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
>>> 
================== RESTART: G:/ProgramsPython/Fibonacci.py ==================
>>> fib(10)
Fibonacci series:
0 
 1
1
2
3
5
8
13
21
>>> 
================== RESTART: G:/ProgramsPython/Fibonacci.py ==================
>>> fib(5,0,1)
Fibonacci series:
0 
 1
1
2
3
5
8
>>> fib(10,3,4)
Fibonacci series:
3 
 4
7
11
18
>>> fib(5,10,11)
Fibonacci series:
10 
 11
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fibonacci(10)
>>> fib(10)
Fibonacci series:
0 
 1
1
2
3
5
8
13
21
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fibonacci(10)
>>> 
>>> fibonacci(10)
>>> fib().fibonacci(10)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    fib().fibonacci(10)
TypeError: fib() missing 1 required positional argument: 'n'
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fibonacci(10)
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fibonacci(10)
[1, 2, 3, 5, 8, 13, 21]
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fibonacci(10)
[1, 2, 3, 5, 8, 13, 21]
>>> fib(5)
Fibonacci series:
0 
 1
1
2
3
5
8
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fibonacci(10)
[0, 1, 1, 2, 3, 5, 8]
>>> fibonacci(15)
[0, 1, 1, 2, 3, 5, 8, 13]
>>> fib()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    fib()
TypeError: fib() missing 1 required positional argument: 'n'
>>> fib
<function fib at 0x000002991A49E1E0>
>>> print(fib)
<function fib at 0x000002991A49E1E0>
>>> print(fib())
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(fib())
TypeError: fib() missing 1 required positional argument: 'n'
>>> print(fib(0))
Fibonacci series:
0 
 1
None
>>> fib(5)
Fibonacci series:
0 
 1
1
2
3
5
8
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fib(5)
Fibonacci series:
0 
 1
0
1
1
2
3
>>> 
================== RESTART: G:\ProgramsPython\Fibonacci.py ==================
>>> fibonacci(20)
[0, 1, 1, 2, 3, 5, 8, 13]
>>> fibonacci(len(range(22)))
[0, 1, 1, 2, 3, 5, 8, 13, 21]
>>> 
