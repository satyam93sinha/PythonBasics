Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> _
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    _
NameError: name '_' is not defined
>>> a=3
>>> b=2
>>> a+b
5
>>> a++
SyntaxError: invalid syntax
>>> a+_
8
>>> 'she said'
'she said'
>>> "quotes too come in output when we enter String directly in Python"
'quotes too come in output when we enter String directly in Python'
>>> python
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> 'if we don\'t include quotes and print command, String is treated as variable'
"if we don't include quotes and print command, String is treated as variable"
>>> 'if we dont include quotes and print command, String is treated as variable'
'if we dont include quotes and print command, String is treated as variable'
>>> s='First  line. Second Line.'
>>> s
'First  line. Second Line.'
>>> 'First  line. \\nSecond Line.'
'First  line. \\nSecond Line.'
>>> s='first line.\\n second line.'
>>> s
'first line.\\n second line.'
>>> s='first line. \n second line.'
>>> s
'first line. \n second line.'
>>> print(s)
first line. 
 second line.
>>> s='first line. second line'
>>> print(s)
first line. second line
>>> print('first line.\n this is treated as special character without raw string')
first line.
 this is treated as special character without raw string
>>> print(r'first line.\n this is treated as special character without raw string')
first line.\n this is treated as special character without raw string
>>> print(r'first line.\n this is not treated as special character if raw string denoted by r is included before quotes')
first line.\n this is not treated as special character if raw string denoted by r is included before quotes
>>> 
