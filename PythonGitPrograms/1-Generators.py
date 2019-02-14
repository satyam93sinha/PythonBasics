Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def reverse(data):
	for i in range(len(data)-1):
		print(i)

		
>>> reverse('data')
0
1
2
>>> 
>>> def reverse(data):
	for i in range(len(data)-1):
		print(data(i))

		
>>> reverse('data')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    reverse('data')
  File "<pyshell#7>", line 3, in reverse
    print(data(i))
TypeError: 'str' object is not callable

>>> def reverse(data):
	for i in (len(data)-1):
		print(data(i))

		
>>> reverse('data')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    reverse('data')
  File "<pyshell#10>", line 2, in reverse
    for i in (len(data)-1):
TypeError: 'int' object is not iterable
>>> # this is integer now, so yes, my bad! Just trying mostly everything one
>>> # would try in every case.
>>> def reverse(data):
	for i in range(len(data)-1):
		print(data[i])

		
>>> reverse('data')
d
a
t
>>> # remember range(start, stop[, step])
>>> def reverse(data):
	for i in range(len(data)-1, -1, -1):
		print(data[i])

		
>>> reverse('data')
a
t
a
d
>>> # this isn't a generator func yet, yields nothing.
>>> def reverse(data):
	for i in range(len(data)-1, -1, -1):
		yield(data[i])

		
>>> rev = reverse('yields reverse')
>>> next(rev)
'e'
>>> next(rev)
's'
>>> next(rev)
'r'
>>> next(rev)
'e'
>>> for i in rev:
	print(i)

	
v
e
r
 
s
d
l
e
i
y
>>> 
