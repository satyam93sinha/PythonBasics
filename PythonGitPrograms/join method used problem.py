Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def concat(*args, sel='/'):
	for i in args:
		print(i,sel)

		
>>> concat('hey','you','going')
hey /
you /
going /
>>> def concat(*args, sel='/'):
	for i in args:
		print(i,end=sel)

		
>>> concat('hey','you','going')
hey/you/going/
>>> def concat(*args, sel='/'):
	for i in args:
		print(i.join(sel))

		
>>> concat('hey','you','going')
/
/
/
>>> def concat(*args, sel='/'):
	for i in args:
		print(args.join(sel))

		
>>> concat('hey','you','going')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    concat('hey','you','going')
  File "<pyshell#12>", line 3, in concat
    print(args.join(sel))
AttributeError: 'tuple' object has no attribute 'join'
>>> def concat(*args, sel='/'):
	for i in args:
		print(sel.join(args))

		
>>> concat('hey','you','going')
hey/you/going
hey/you/going
hey/you/going
>>> 
