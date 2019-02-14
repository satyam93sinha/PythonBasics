Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'hello'
>>> s_2 = 'world'
>>> print('{0}, {1}'.format(s, s_2))
hello, world
>>> print('{}, {}'.format(s, s_2))
hello, world
>>> # The brackets and characters within them (called format ﬁelds) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.
>>> print('{1st_word}, {2nd_word}'.format('1st_word':s, '2nd_word':s_2))
SyntaxError: invalid syntax
>>> print('{1st_word}, {2nd_word}'.format(1st_word:s, 2nd_word:s_2))
SyntaxError: invalid syntax
>>> print('{1st_word}, {2nd_word}'.format(1st_word=s, 2nd_word=s_2))
SyntaxError: invalid syntax
>>> print('{word1}, {word2}'.format(word1=s, word2=s_2))
hello, world
>>> print('{1word}, {2word}'.format(1word=s, 2word=s_2))
SyntaxError: invalid syntax
>>> # keyword argument can't start with a number.
>>> print('{word1}, {1}'.format(word1=s, word2=s_2))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print('{word1}, {1}'.format(word1=s, word2=s_2))
IndexError: tuple index out of range
>>> print('{word1}, {1}'.format(word1=s, s_2))
SyntaxError: positional argument follows keyword argument
>>> 
>>> print('{1}, {word2}'.format(1=s, word2=s_2))
SyntaxError: keyword can't be an expression
>>> print('{1}, {word2}'.format(s, word2=s_2))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('{1}, {word2}'.format(s, word2=s_2))
IndexError: tuple index out of range
>>> print('{0}, {word2}'.format(s, word2=s_2))
hello, world
>>> # .format(*args) and as we already know (*args) takes tuple as input, thus   when we put {1} the index of tuple is taken as 1 which is out of range bcoz the keyword argument already is defined with its value, so correct would be to      refer to the tuple according to its index.
>>> print('{1}, {0}'.format(s, s_2))
world, hello
>>> # I hope I have clarified the last comment.
>>> print('{!s}, {!r}'.format(s, s_2))
hello, 'world'
>>> print('{!a}, {!r}'.format(s, s_2))
'hello', 'world'
>>> # !a, !s,!r to convert values to ascii, str() and repr() strings before they are formatted.
>>> print('{0:!a}, {!s}'.format(s, s_2))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('{0:!a}, {!s}'.format(s, s_2))
ValueError: Invalid format specifier
>>> import math
>>> print('{0:.3f}'.format(math.pi))
3.142
>>> math.pi
3.141592653589793
>>> # the actual value of math.pi is shown above which gets formatted to 3       decimal places through .format() and optional use of ":" with format specifier.
>>> print('{0:5f}'.format(1234567890))
1234567890.000000
>>> print('{0:5}'.format(1234567890))
1234567890
>>> print('{0:5}'.format(123))
  123
>>> # Passing an integer after the ':' will cause that ﬁeld to be a minimum number of characters wide. Useful for making tables pretty.
>>> table = {'Jack':1234, 'Shaun':3232, 'Evelyn':39884}
>>> type(table)
<class 'dict'>
>>> for name, phone in table.items():
	print('Evelyn:{[Evelyn]}', 'Shaun:{[Shaun]}','Jack:{[Jack]}'.format(table))

	
Evelyn:{[Evelyn]} Shaun:{[Shaun]} Jack:1234
Evelyn:{[Evelyn]} Shaun:{[Shaun]} Jack:1234
Evelyn:{[Evelyn]} Shaun:{[Shaun]} Jack:1234
>>> for name, phone in table.items():
	print('Evelyn:{[Evelyn]}', 'Shaun:{[Shaun]}','Jack:{[Jack]}'.format(**table))

	
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print('Evelyn:{[Evelyn]}', 'Shaun:{[Shaun]}','Jack:{[Jack]}'.format(**table))
IndexError: tuple index out of range
>>> for name, phone in table.items():
	print('Evelyn:{Evelyn}', 'Shaun:{Shaun}','Jack:{Jack}'.format(**table))

	
Evelyn:{Evelyn} Shaun:{Shaun} Jack:1234
Evelyn:{Evelyn} Shaun:{Shaun} Jack:1234
Evelyn:{Evelyn} Shaun:{Shaun} Jack:1234
>>> for name, phone in table.items():
	print('Evelyn:{Evelyn}', 'Shaun:{Shaun}','Jack:{Jack}'.format(name,phone))

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    print('Evelyn:{Evelyn}', 'Shaun:{Shaun}','Jack:{Jack}'.format(name,phone))
KeyError: 'Jack'
>>> for name, phone in table.items():
	print('Evelyn:{Evelyn}', 'Shaun:{Shaun}','Jack:{Jack}'.format(phone))

	
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    print('Evelyn:{Evelyn}', 'Shaun:{Shaun}','Jack:{Jack}'.format(phone))
KeyError: 'Jack'
>>> for name, phone in table.items():
	print('{0}, {1}'.format(name,phone))

	
Jack, 1234
Shaun, 3232
Evelyn, 39884
>>> # loops sequentially, not possible to reorder or randomly display keys:value  pair
>>> print('Evelyn:{Evelyn}',
	  'Jack: {Jack}',
	  'Shaun:{Shaun}'.format(table))
Traceback (most recent call last):
  File "<pyshell#51>", line 3, in <module>
    'Shaun:{Shaun}'.format(table))
KeyError: 'Shaun'
>>> print('Evelyn:{Evelyn}',
	  'Jack: {Jack}',
	  'Shaun:{Shaun}'.format(**table))
Evelyn:{Evelyn} Jack: {Jack} Shaun:3232
>>> # it is displayed this way bcoz we have added .format with 'Shaun:{Shaun}'   string only.
>>> print('Evelyn:{Evelyn},
	  'Jack: {Jack},
	  'Shaun:{Shaun}'.format(**table))
SyntaxError: EOL while scanning string literal
>>> print('Evelyn:{Evelyn},
	  'Jack: {Jack},Shaun:{Shaun}'.format(**table))
SyntaxError: EOL while scanning string literal
>>> print('Evelyn:{Evelyn},Jack: {Jack},Shaun:{Shaun}'.format(**table))
Evelyn:39884,Jack: 1234,Shaun:3232
>>> print('Evelyn:{Evelyn},Jack: {Jack},Shaun:{Shaun}'.format(table))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print('Evelyn:{Evelyn},Jack: {Jack},Shaun:{Shaun}'.format(table))
KeyError: 'Evelyn'
>>> print('Jack: {Jack},Shaun:{Shaun},Evelyn:{Evelyn}'.format(table))
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print('Jack: {Jack},Shaun:{Shaun},Evelyn:{Evelyn}'.format(table))
KeyError: 'Jack'
>>> # KeyError bcoz we haven't unpacked the dict table.
>>> # **table is used to unpack the dict (table object)
>>> print('Jack: {[Jack]},Shaun:{[Shaun]},Evelyn:{[Evelyn]}'.format(table))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print('Jack: {[Jack]},Shaun:{[Shaun]},Evelyn:{[Evelyn]}'.format(table))
IndexError: tuple index out of range
>>> # tuple indices are integers but the indices mentioned here aren't numbers.
>>> print('Jack: {0[Jack]},Shaun:{1[Shaun]},Evelyn:{2[Evelyn]}'.format(table))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print('Jack: {0[Jack]},Shaun:{1[Shaun]},Evelyn:{2[Evelyn]}'.format(table))
IndexError: tuple index out of range
>>> print('Jack: {0[Jack]},Shaun:{0[Shaun]},Evelyn:{0[Evelyn]}'.format(table))
Jack: 1234,Shaun:3232,Evelyn:39884
>>> # the above code references variables by name instead of by position, refer  to 24-Fancier Output Formatting.txt
>>> 
