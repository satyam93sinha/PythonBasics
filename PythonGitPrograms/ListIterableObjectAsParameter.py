Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list((1,2,3))
[1, 2, 3]
>>> list((1))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    list((1))
TypeError: 'int' object is not iterable
>>> list(('string'))
['s', 't', 'r', 'i', 'n', 'g']
>>> 
