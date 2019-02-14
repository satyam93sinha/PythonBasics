def ok_prompt(prompt,retries=4,reminder='Please try again'):
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
ok_prompt('nothing').__annotations__
