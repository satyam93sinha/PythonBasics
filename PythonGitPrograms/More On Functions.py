Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return True
		retries=retries-1
		if retries<0:
			print("invalid response")
		print(reminder)

		
>>> ok_prompt("Do you wish to continue?")
Do you wish to continue?y
True
>>> ok_prompt("Do you wish to continue?",0,"Don't try more than once!")
Do you wish to continue?ye
True
>>> ok_prompt("Do you wish to continue?",0,"Don't try more than once!")
Do you wish to continue?nop
True
>>> ok_prompt("Do you wish to continue?",-1,"Don't try more than once!")
Do you wish to continue?ye
True
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			print("invalid response")
		print(reminder)

		
>>> ok_prompt("Do you wish to continue?",0,"Don't try more than once!")
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?
invalid response
Don't try more than once!
Do you wish to continue?y
True
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			print("invalid response")
			if reminder in ("Don't try more than once","Exhausted",
					"Limit Exceeded"):
				print(reminder)
			else:
				return reminder

			
>>> ok_prompt("Do you wish to continue?",0,"Don't try more than once!")
Do you wish to continue?
invalid response
"Don't try more than once!"
>>> ok_prompt("Do you wish to continue?",0,"Don't try more than once!")def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			print("invalid response")
			if reminder in ("Don't try more than once","Exhausted",
					"Limit Exceeded"):
				print(reminder)
			elif retries in (0):
				return ('Trial Limit Exceeded')
			
SyntaxError: invalid syntax
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			print("invalid response")
			if reminder in ("Don't try more than once","Exhausted",
					"Limit Exceeded"):
				print(reminder)
			elif retries in (0):
				return ("Trial Limit Exceeded")

			
>>> ok_prompt("Do you wish to continue?",0)
Do you wish to continue?
invalid response
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ok_prompt("Do you wish to continue?",0)
  File "<pyshell#29>", line 14, in ok_prompt
    elif retries in (0):
TypeError: argument of type 'int' is not iterable
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			raise ValueError("invalid response")
		print(reminder)

		
>>> ok_prompt("Do you wish to continue?",0)
Do you wish to continue?
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ok_prompt("Do you wish to continue?",0)
  File "<pyshell#33>", line 10, in ok_prompt
    raise ValueError("invalid response")
ValueError: invalid response
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			raise ValueError("invalid response")
	print(reminder)

	
>>> ok_prompt("Do you wish to continue?",0)
Do you wish to continue?
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ok_prompt("Do you wish to continue?",0)
  File "<pyshell#36>", line 10, in ok_prompt
    raise ValueError("invalid response")
ValueError: invalid response
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			return("invalid response")
	print(reminder)

	
>>> ok_prompt("Do you wish to continue?",0)
Do you wish to continue?
'invalid response'
>>> def ok_prompt(prompt,retries=4,reminder='Please try again'):
	while True:
		ok=input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries=retries-1
		if retries<0:
			return("invalid response")
print(reminder)
SyntaxError: invalid syntax
>>> 
