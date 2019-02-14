Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in [3.4,4]:
	print(i)

	
3.4
4
>>> dir(for)
SyntaxError: invalid syntax
>>> 
>>> # for is not an object so SyntaxError
>>> i = {2:4, 3:9}
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    next(i)
TypeError: 'dict' object is not an iterator
>>> # first will have to call the iter() method, which will in turn let us
>>> # call the next() method.
>>> j = iter(i)
>>> next(j)
2
>>> next(j)
3
>>> next(j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    next(j)
StopIteration
>>> # returns keys, because there is only one iterable object according to
>>> # j = iter(i) returns only one iterable. Later, StopIteration
>>> # when iteration gets exhausted or comes to an end.
>>> # In this sequence, next() method returns the elements of iterable object
>>> # from beginning until end, thus, from 0th index to last index.
>>> class Reverse:
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		print(self)
		return self
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index-1
		return self.data[self.index]

	
>>> rev = Reverse([1,2,3])
>>> rev.__iter__()
<__main__.Reverse object at 0x03290190>
<__main__.Reverse object at 0x03290190>
>>> Reverse.__iter__([1,3,2])
[1, 3, 2]
[1, 3, 2]
>>> # Thus, __iter__(self) method here simply stores the iterable object.
>>> revr = iter(rev)
<__main__.Reverse object at 0x03290190>
>>> next(revr)
3
>>> next(revr)
2
>>> next(revr)
1
>>> next(revr)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    next(revr)
  File "<pyshell#32>", line 10, in __next__
    raise StopIteration
StopIteration
>>> # Now when we call iter() method, an object location is returned
>>> # later it allows us calling next() method which reverses the object
>>> # because we have changed the functionality of iter() here for this class.
>>> for i in rev:
	print(i)

	
<__main__.Reverse object at 0x03290190>
>>> for i in revr:
	print(i)

	
<__main__.Reverse object at 0x03290190>
>>> for list_ in rev:
	print(list_)

	
<__main__.Reverse object at 0x03290190>
>>> rev = Reverse("spam")
>>> iter(rev)
<__main__.Reverse object at 0x03290750>
<__main__.Reverse object at 0x03290750>
>>> for i in rev:
	print(i)

	
<__main__.Reverse object at 0x03290750>
m
a
p
s
>>> rev = Reverse({1:1, 2:4})
>>> for i in rev:
	print(i)

	
<__main__.Reverse object at 0x03290610>
1
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    for i in rev:
  File "<pyshell#32>", line 12, in __next__
    return self.data[self.index]
KeyError: 0
>>> # doesn't have any index but key so this reversal searches for 0 as Key and
>>> # raises KeyError exception when not found.
>>> # dict doesn't have any index, its key and value pair.
>>> class Reverse:
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index-1
		return self.data[self.index]

	
>>> rev = Reverse("sap")
>>> for i in rev:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    for i in rev:
TypeError: 'Reverse' object is not iterable
>>> iter(rev)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    iter(rev)
TypeError: 'Reverse' object is not iterable
>>> # First and foremost, we need iter() method which routes the call to next()
>>> # method. Here, in above program there's no __iter__() defined which is why
>>> # __next__() isn't called and thus, Reverse is not iterable.
>>> # We conclude that way of call is iter() method then next() method.
>>> # iter() and next() are built-in methods.
>>> class Reverse:
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		print(self)
		return self

	
>>> rev = Reverse("sap")
>>> iter(rev)
<__main__.Reverse object at 0x00A31830>
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    iter(rev)
TypeError: iter() returned non-iterator of type 'Reverse'
>>> for i in rev:
	print(i)

	
<__main__.Reverse object at 0x00A31830>
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    for i in rev:
TypeError: iter() returned non-iterator of type 'Reverse'
>>> # Here, iter() method's presence is unable to iterate over the object
>>> # argument passed without the definition of next() method.
>>> # Thus, here object location is returned with non-iterator of type 'Reverse'
>>> # Non-iterator of type 'Reverse' means class is Reverse, iter() returned a
>>> # non-iterator because it didn't find __next__() to iterate.
