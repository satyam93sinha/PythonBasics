Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def arguments(types,*args,**kwargs):
	print('Type of argument called:',types)
	for i in args:
		print(i,':\t',args[i])

		
>>> arguments('positional','directly','passing','arguments','to formal parameters')
Type of argument called: positional
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    arguments('positional','directly','passing','arguments','to formal parameters')
  File "<pyshell#4>", line 4, in arguments
    print(i,':\t',args[i])
TypeError: tuple indices must be integers or slices, not str
#for i in range(len(args)): will work.
>>> arguments('positional',1,2,2,3)
Type of argument called: positional
1 :	 2
2 :	 2
2 :	 2
3 :	 3
>>> arguments('positional',(1,2,2,3))
Type of argument called: positional
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    arguments('positional',(1,2,2,3))
  File "<pyshell#4>", line 4, in arguments
    print(i,':\t',args[i])
TypeError: tuple indices must be integers or slices, not tuple
>>> def arguments(types,*args,**kwargs):
	print('Type of argument called:',types)
	for i in args:
		print(i)
	for kw in kwargs:
		print(kw,':\t',kwargs[kw])

		
>>> arguments('positional','directly','passing','arguments','to formal parameters')
Type of argument called: positional
directly
passing
arguments
to formal parameters
>>> arguments('positional',way='passing',kind='arguments',where='to final formal parameters')
Type of argument called: positional
way :	 passing
kind :	 arguments
where :	 to final formal parameters
>>> def arguments(types,*args,**kwargs):
	print('Type of argument called:',types)
	for i in args:
		print(i,':\t',args)

		
>>> arguments('positional','directly','passing','arguments','to formal parameters')
Type of argument called: positional
directly :	
 ('directly', 'passing', 'arguments', 'to formal parameters')
passing :	 ('directly', 'passing', 'arguments', 'to formal parameters')
arguments :	 ('directly', 'passing', 'arguments', 'to formal parameters')
to formal parameters :	 ('directly', 'passing', 'arguments', 'to formal parameters')
>>> def arguments(types,*args,**kwargs):
	print('Type of argument called:',types)
	for __ in args:
		print(__,':\t',args)

		
>>> arguments('positional','directly','passing','arguments','to formal parameters')
Type of argument called: positional
directly :	 ('directly', 'passing', 'arguments', 'to formal parameters')
passing :	 ('directly', 'passing', 'arguments', 'to formal parameters')
arguments :	 ('directly', 'passing', 'arguments', 'to formal parameters')
to formal parameters :	 ('directly', 'passing', 'arguments', 'to formal parameters')
>>> def arguments(types,*args,**kwargs):
	print('Type of argument called:',types)
	for __ in args:
		print(__,':\t',args[__])

		
>>> arguments('positional','directly','passing','arguments','to formal parameters')
Type of argument called: positional
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    arguments('positional','directly','passing','arguments','to formal parameters')
  File "<pyshell#21>", line 4, in arguments
    print(__,':\t',args[__])
TypeError: tuple indices must be integers or slices, not str
>>> 
