Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> months
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    months
NameError: name 'months' is not defined
>>> months=['Jan','Feb','March','4']
>>> months
['Jan', 'Feb', 'March', '4']
>>> months=months[0:2]
>>> months
['Jan', 'Feb']
>>> months=months[0:3]
>>> months
['Jan', 'Feb']
>>> months+['March','April','May',"june"]
['Jan', 'Feb', 'March', 'April', 'May', 'june']
>>> months
['Jan', 'Feb']
>>> months+=['March','April','May',"june"]
>>> months
['Jan', 'Feb', 'March', 'April', 'May', 'june']
>>> letters=['a',2]
>>> letters
['a', 2]
>>> months
['Jan', 'Feb', 'March', 'April', 'May', 'june']
>>> months[0]=1
>>> months
[1, 'Feb', 'March', 'April', 'May', 'june']
>>> months.append('July')
>>> months
[1, 'Feb', 'March', 'April', 'May', 'june', 'July']
>>> len(months)
7
>>> months[2:4]=[]
>>> months
[1, 'Feb', 'May', 'june', 'July']
>>> a,b=0,1
>>> while(b<20)
SyntaxError: invalid syntax
>>> while(b<20):
	print(b)
	a,b=b,a+b

	
1
1
2
3
5
8
13
>>> a
13
>>> b
21
>>> c=0
>>> d=1
>>> print(c)
0
>>> print(d)
1
>>> c=d
>>> d=c+d
>>> print(c)
1
>>> print(d)
2
>>> c=0
>>> d=1
>>> c,d=d,c+d
>>> print(c,d)
1 1
>>> while(b<40):
	print(b)
	a,b=b,a+b

	
21
34
>>> a,b=0,1
while(b<40):
	print(b)
	a,b=b,a+b
	
SyntaxError: multiple statements found while compiling a single statement
>>> a,b=0,1
>>> while(b<40):
	print(b)
	a,b=b,a+b

	
1
1
2
3
5
8
13
21
34
>>> 
