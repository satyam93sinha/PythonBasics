Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for item in [2,3,4]:
	print(item)

	
2
3
4
>>> next([2,3,4])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    next([2,3,4])
TypeError: 'list' object is not an iterator
>>> l = [2,3,4]
>>> next(l)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    next(l)
TypeError: 'list' object is not an iterator
>>> i = iter(l)
>>> i
<list_iterator object at 0x032A0150>
>>> next(i)
2
>>> next(i)
3
>>> next(i)
4
>>> # for statement ultimately calls iter() which as shown above creates an
>>> # object and then calls __next__() which accesses elements in container
>>> # one at a time.
>>> # When there are no elements in container, __next__() raises StopIteration
>>> # exception which tells for loop to terminate.
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    next(i)
StopIteration
>>> 
