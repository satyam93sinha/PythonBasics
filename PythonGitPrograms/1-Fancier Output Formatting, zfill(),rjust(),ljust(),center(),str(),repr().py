Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type(string)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    type(string)
NameError: name 'string' is not defined
>>> type(str)
<class 'type'>
>>> s = 'Hello, world'
>>> type(s)
<class 'str'>
>>> str(s)
'Hello, world'
>>> s
'Hello, world'
>>> s_2 = "Hey, what's the difference"
>>> s_2
"Hey, what's the difference"
>>> repr(s)
"'Hello, world'"
>>> type(s)
<class 'str'>
>>> type(repr(s))
<class 'str'>
>>> type(str(s))
<class 'str'>
>>> str(s)
'Hello, world'
>>> str(s_2)
"Hey, what's the difference"
>>> repr(s_2)
'"Hey, what\'s the difference"'
>>> # str() returns representation for fairly human-readable
>>> # repr() generate representations which can be read by interpreter
>>> str(1/7)
'0.14285714285714285'
>>> repr(1/7)
'0.14285714285714285'
>>> # No specific representation for human-consumption so str() and repr() give
>>> # same output for str(1/7) and repr(1/7)
>>> x = 3.25
>>> x = 2.32*10
>>> y = 40**2
>>> result = 'The result of x:' + repr(x) + 'and y:' + str(y)
>>> result
'The result of x:23.2and y:1600'
>>> result = 'The result of x:' + repr(x) + 'and y:' + str(y) + '\n line change
SyntaxError: EOL while scanning string literal
>>> result = 'The result of x:' + repr(x) + 'and y:' + str(y) + '\n line change'
>>> result
'The result of x:23.2and y:1600\n line change'
>>> result = 'The result of x:' + repr(x) + 'and y:' + repr(y) + '\n line change'
>>> result
'The result of x:23.2and y:1600\n line change'
>>> str(result)
'The result of x:23.2and y:1600\n line change'
>>> print(result)
The result of x:23.2and y:1600
 line change
>>> # the repr() and str() adds string quotes and backslashes, no line change is seen in the above context, but when print() is used, the output depicts change
>>> for x in range(1,11):
	print(repr(x), repr(x**2), repr(x**3))

	
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
>>> for x in range(1,11):
	print(repr(x),rjust(2), repr(x**2).rjust(3), repr(x**3))

	
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print(repr(x),rjust(2), repr(x**2).rjust(3), repr(x**3))
NameError: name 'rjust' is not defined
>>> for x in range(1,11):
	print(repr(x).rjust(2), repr(x**2).rjust(3), repr(x**3))

	
 1   1 1
 2   4 8
 3   9 27
 4  16 64
 5  25 125
 6  36 216
 7  49 343
 8  64 512
 9  81 729
10 100 1000
>>> for x in range(1,11):
	print(repr(x).rjust(2), repr(x**2).rjust(3), repr(x**3).rjust(4))

	
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>> for x in range(1,11):
	print(str(x).rjust(2), str(x**2).rjust(3), repr(x**3).rjust(4))

	
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>> for x in range(1,11):
	print(str(x).rjust(2), str(x**2).rjust(3), str(x**3).rjust(4))

	
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>> for x in range(1,11):
	print(str(x).rjust(2,0), str(x**2).rjust(3,0), str(x**3).rjust(4,0))

	
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    print(str(x).rjust(2,0), str(x**2).rjust(3,0), str(x**3).rjust(4,0))
TypeError: The fill character must be a unicode character, not int
>>> for x in range(1,11):
	print(str(x).rjust(2,'0'), str(x**2).rjust(3), str(x**3).rjust(4))

	
01   1    1
02   4    8
03   9   27
04  16   64
05  25  125
06  36  216
07  49  343
08  64  512
09  81  729
10 100 1000
>>> # string.rjust(length,fillchar), string.ljust(length,fillchar) are syntax
>>> # returns new string with fixing length of string to mentioned in parameter,
>>> # if the string has length less than length parameter, fillchar positional
>>> # argument is used to fill in the space as shown in above example, i.e,01 09
>>> repr([1,3])
'[1, 3]'
>>> str((1,3))
'(1, 3)'
>>> # any object can be converted to string through repr() and str()
>>> # any values can be converted to string through repr() and str()
>>> for x in range(1,11):
	print(str(x).zfill(2), str(x**2).zfill(3), str(x**3).rjust(4))

	
01 001    1
02 004    8
03 009   27
04 016   64
05 025  125
06 036  216
07 049  343
08 064  512
09 081  729
10 100 1000
>>> # string.zfill() fills the left-end of string with zeros, understands + and - signs, pads the numeric string with zeros in the left.
>>> s.zfill(30)
'000000000000000000Hello, world'
>>> s.rjust(3)
'Hello, world'
>>> s.ljust(10)
'Hello, world'
>>> s.ljsut(30,*)
SyntaxError: invalid syntax
>>> s.ljust(30,*)
SyntaxError: invalid syntax
>>> s.ljust(30,'*')
'Hello, world******************'
>>> s.center(30,'*;')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.center(30,'*;')
TypeError: The fill character must be exactly one character long
>>> s.center(30,'*')
'*********Hello, world*********'
>>> s.rjust(30,'*')
'******************Hello, world'
>>> '13'.zfill(4)
'0013'
>>> '13'.rjust(4)
'  13'
>>> '13'.ljust(4)
'13  '
>>> '-13'.zfill(4)
'-013'
>>> '-13'.rjust(5)
'  -13'
>>> '-13'.rjust(5,'*')
'**-13'
>>> '-13'.ljust(5,'_')
'-13__'
>>> # except string.zfill() no other among zfill(), rjust() and ljust()
>>> # understands + and - signs as proved through above examples.
>>> 
