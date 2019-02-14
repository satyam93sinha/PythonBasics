Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list.extend(2,3,5)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    list.extend(2,3,5)
TypeError: descriptor 'extend' requires a 'list' object but received a 'int'
>>> a=[2,3,4]
>>> a.extend(5,6)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.extend(5,6)
TypeError: extend() takes exactly one argument (2 given)
>>> a.extend([5,6])
>>> a
[2, 3, 4, 5, 6]
>>> a.extend((5,6))
>>> a
[2, 3, 4, 5, 6, 5, 6]
>>> a[len(a):]=['e','f']
>>> a
[2, 3, 4, 5, 6, 5, 6, 'e', 'f']
>>> a.insert(3,'g')
>>> a
[2, 3, 4, 'g', 5, 6, 5, 6, 'e', 'f']
>>> a.insert(len(a),'h')
>>> a
[2, 3, 4, 'g', 5, 6, 5, 6, 'e', 'f', 'h']
>>> # this above insert works similar to a.append(x), bcoz we are adding 'h' to the end of the list a
>>> insert
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    insert
NameError: name 'insert' is not defined
>>> a.insert()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.insert()
TypeError: insert() takes exactly 2 arguments (0 given)
>>> type(insert())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(insert())
NameError: name 'insert' is not defined
>>> type(a.insert(0,3))
<class 'NoneType'>
>>> a.remove(5)
>>> a
[3, 2, 3, 4, 'g', 6, 5, 6, 'e', 'f', 'h']
>>> a.remove(3)
>>> a
[2, 3, 4, 'g', 6, 5, 6, 'e', 'f', 'h']
>>> a.remove('i')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.remove('i')
ValueError: list.remove(x): x not in list
>>> a.pop()
'h'
>>> a
[2, 3, 4, 'g', 6, 5, 6, 'e', 'f']
>>> # a.pop([index]) removes and returns element present at specified index, index is optional thus it's present in [], if we don't specify index, pop will remove and return the last item of the list.
>>> a.pop(5)
5
>>> a
[2, 3, 4, 'g', 6, 6, 'e', 'f']
>>> # first 5 encountered is removed.
>>> a.clear()
>>> a
[]
>>> del a[:]
>>> a
[]
>>> a=[1,2]
>>> del a[:]
>>> a
[]
>>> a.index(5[,0[,3])
	    
SyntaxError: invalid syntax
>>> a.index(5[0[,3])
	    
SyntaxError: invalid syntax
>>> a.index(5[0[3])
	    
SyntaxError: invalid syntax
>>> a.index(5[,0[,3]])
	    
SyntaxError: invalid syntax
>>> a[len(a):]=['e','f']
	    
>>> a
	    
['e', 'f']
>>> a.index('f'[,0[,2]])
	    
SyntaxError: invalid syntax
>>> a.index('f'[0[2]])
	    
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.index('f'[0[2]])
TypeError: 'int' object is not subscriptable
>>> a.index('f'[0:2])
	    
1
>>> a.extend(3,5,3,5,3)
	    
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.extend(3,5,3,5,3)
[TypeError: extend() takes exactly one argument (5 given)
>>> a
 
['e', 'f']
>>> a.extend([3,4,3,3,3,3])
 
[
>>> a
['e', 'f', 3, 4, 3, 3, 3, 3]
>>> a.count(3)
5
>>> a.count('e')
1
>>> a.index([3:6])
SyntaxError: invalid syntax
>>> a.index(3[3:6])
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.index(3[3:6])
TypeError: 'int' object is not subscriptable
>>> a.index(3[,start[,end]])
SyntaxError: invalid syntax
>>> a.index(3[:])
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.index(3[:])
TypeError: 'int' object is not subscriptable
>>> a.index(3[:])
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.index(3[:])
TypeError: 'int' object is not subscriptable
>>> a.index('3'[:])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.index('3'[:])
ValueError: '3' is not in list
>>> a
['e', 'f', 3, 4, 3, 3, 3, 3]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a.remove('e')
>>> a.remove('f')
>>> a
[3, 4, 3, 3, 3, 3]
>>> a.sort()
>>> a
[3, 3, 3, 3, 3, 4]
>>> a.sort(key=None,reverse=False)
>>> a
[3, 3, 3, 3, 3, 4]
>>> a.sort(key=None,reverse=True)
>>> a
[4, 3, 3, 3, 3, 3]
>>> a.sort(key=str,reverse=True)
>>> a
[4, 3, 3, 3, 3, 3]
>>> type(a[0])
<class 'int'>
>>> a.reverse()
>>> a
[3, 3, 3, 3, 3, 4]
>>> #reverses list
>>> a.copy()
[3, 3, 3, 3, 3, 4]
>>> b=a.copy()
>>> a
[3, 3, 3, 3, 3, 4]
>>> b
[3, 3, 3, 3, 3, 4]
>>> # a.copy() returns shallow copy of list, equivalent to a[:]
>>> fruits=['apple','banana','grapes']
>>> fruits.append('mango','apple')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    fruits.append('mango','apple')
TypeError: append() takes exactly one argument (2 given)
>>> fruits.append('mango')
>>> fruits.copy()
['apple', 'banana', 'grapes', 'mango']
>>> fruits.extend(['cherry','blueberry'])
>>> fruits
['apple', 'banana', 'grapes', 'mango', 'cherry', 'blueberry']
>>> fruits.insert(5,'apple')
>>> fruits
['apple', 'banana', 'grapes', 'mango', 'cherry', 'apple', 'blueberry']
>>> fruits.index('grapes',3)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    fruits.index('grapes',3)
ValueError: 'grapes' is not in list
>>> # searches the sub-sequence of list, starting from index 3 or 'mango', when no 'grapes' is found throughout the list, returns not in list
>>> fruits.index('apple',5)
5
>>> fruits.index('apple',4)
5
>>> # finds 'apple' and returns the index.
>>> fruits.count('apple')
2
>>> fruits.reverse()
>>> fruits
['blueberry', 'apple', 'cherry', 'mango', 'grapes', 'banana', 'apple']
>>> fruits.pop(5)
'banana'
>>> fruits.pop()
'apple'
>>> fruits
['blueberry', 'apple', 'cherry', 'mango', 'grapes']
>>> fruits.clear()
>>> fruits
[]
>>> fruits.append('mango')
>>> fruits
['mango']
>>> fruits.remove()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    fruits.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> fruits.remove('mango')
>>> fruits
[]
>>> fruits.extend(['apple','banana'])
>>> fruits
['apple', 'banana']
>>> del fruits[:]
>>> fruits
[]
>>> stack=[3,4,5]
>>> stack.append(6)
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack
[3, 4, 5]
>>> 
