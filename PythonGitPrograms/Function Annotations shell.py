Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def functional_annotations(studio: Marvel, movie: str='Avengers:Infinity War')->str:
	print(studio,functional_annotations.__annotations__)

	
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    def functional_annotations(studio: Marvel, movie: str='Avengers:Infinity War')->str:
NameError: name 'Marvel' is not defined
>>> def functional_annotations(studio: str, movie: str='Avengers:Infinity War')->str:
	print(studio,functional_annotations.__annotations__)

	
>>> functional_annotations("Marvel Studios")
Marvel Studios {'studio': <class 'str'>, 'movie': <class 'str'>, 'return': <class 'str'>}
>>> a=[1,2,3]
>>> a[len(a):]=[5]
>>> a
[1, 2, 3, 5]
>>> print([len(a):])
SyntaxError: invalid syntax
>>> len(a)
4
>>> a[len(a)-1:]=[8]
>>> a
[1, 2, 3, 8]
>>> 
