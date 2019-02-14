Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import glob
>>> print(glob.escape.__doc__)
Escape all special characters.
    
>>> print(glob.iglob.__doc__)
Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    
>>> print(glob.glob.__doc__)
Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    
>>> glob.escape("skldlksdlk@#%")
'skldlksdlk@#%'
>>> glob.escape("F://today@#")
'F://today@#'
>>> glob.escape("G://CollegiateSocialConnect")
'G://CollegiateSocialConnect'
>>> print(glob.escape(os.system("dir G://CollegiateSocialConnect")))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(glob.escape(os.system("dir G://CollegiateSocialConnect")))
NameError: name 'os' is not defined
>>> import os
>>> 
>>> print(os.DirEntry.__doc__)
None
>>> print(os.F_OK.__doc__)
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> os.F_OK()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    os.F_OK()
TypeError: 'int' object is not callable
>>> os.F_OK("s")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    os.F_OK("s")
TypeError: 'int' object is not callable
>>> int('s')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int('s')
ValueError: invalid literal for int() with base 10: 's'
>>> int('s', base=0)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int('s', base=0)
ValueError: invalid literal for int() with base 0: 's'
>>> int('0xAE', base=16)
174
>>> 1014/16
63.375
>>> 1014%16
6
>>> 16**1+16**0
17
>>> 10*16**1+14*16**0
174
>>> print(os.O_APPEND.__doc__)
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> def sys_module_(num, even, odd):
	print(num, even, odd)

	
>>> sys_module_(1, 2, 3)
1 2 3
>>> import sys
>>> sys.argv
['']
>>> print(sys_module_(sys.argv))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(sys_module_(sys.argv))
TypeError: sys_module_() missing 2 required positional arguments: 'even' and 'odd'
>>> sys.argv
['']
>>> sys.argv[0]
''
>>> # will see more about Command Line arguments later
>>> import math
>>> print(math.acos.__doc__)
Return the arc cosine (measured in radians) of x.
>>> math.acos(32)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    math.acos(32)
ValueError: math domain error
>>> math.acos(x=32)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    math.acos(x=32)
TypeError: acos() takes no keyword arguments
>>> x = 32
>>> math.acos(x)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    math.acos(x)
ValueError: math domain error
>>> 
