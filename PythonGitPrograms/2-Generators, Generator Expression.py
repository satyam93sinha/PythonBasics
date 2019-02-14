Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list_ = [1,2,3]
>>> sum(x**2 for x in list_)
14
>>> def square_sum():
	list_ = [1,2,3]
	sum_ = 0
	for x in list_:
		print(x)
		sq = x**2
		print(sq)
		sum_ = sum_+sq
		yield sum_

		
>>> sq_sum = square_sum()
>>> next(sq_sum)
1
1
1
>>> next(sq_sum)
2
4
5
>>> next(sq_sum)
3
9
14
>>> def square_sum():
	list_ = [1,2,3]
	sum_ = 0
	for x in list_:
		print("x:{}".format(x))
		sq = x**2
		print("square of x:{}".format(sq))
		sum_ = sum_+sq
		yield "sum:{}".format(sum_)

		
>>> sq_sum = square_sum()
>>> next(sq_sum)
x:1
square of x:1
'sum:1'
>>> next(sq_sum)
x:2
square of x:4
'sum:5'
>>> next(sq_sum)
x:3
square of x:9
'sum:14'
>>> next(sq_sum)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    next(sq_sum)
StopIteration
>>> import os
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Users\\Sinha\\AppData\\Local\\Programs\\Python\\Python37-32'
>>> from os import *
>>> os.getcwd()
'C:\\Users\\Sinha\\AppData\\Local\\Programs\\Python\\Python37-32'
>>> 
