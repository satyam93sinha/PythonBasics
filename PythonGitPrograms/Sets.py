Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """Sets
    Operations and other details"""
'Sets\n    Operations and other details'
>>> cycle = {'tyre','tyre','cadence','pedal','cadence','seat'}
>>> type(cycle)
<class 'set'>
>>> set(cycle)
{'cadence', 'seat', 'pedal', 'tyre'}
>>> cycle
{'cadence', 'seat', 'pedal', 'tyre'}
>>> cycle = {'tyre','tyre','cadence','pedal','cadence','seat'}
>>> cycle
{'cadence', 'seat', 'pedal', 'tyre'}
>>> mall = {'dress','books','utensils','furniture','dress','books'}
>>> type(mall)
<class 'set'>
>>> mall
{'dress', 'books', 'utensils', 'furniture'}
>>> # No duplicate elements, if it was entered duplicate ones are eliminated.
>>> cycle - mall
{'cadence', 'seat', 'pedal', 'tyre'}
>>> # all the elements of cycle not present in mall are displayed
>>> mall - cycle
{'dress', 'books', 'utensils', 'furniture'}
>>> cycle|mall
{'books', 'pedal', 'furniture', 'cadence', 'dress', 'seat', 'tyre', 'utensils'}
>>> # | is or in binary, performs or operation so in case of sets performs union
>>> cycle & mall
set()
>>> #intersection is empty because there's no common element in cycle and mall
>>> car = set(['tyre','tyre','tyre','tyre','music','seat','gear','wheel'])
>>> car
{'gear', 'music', 'wheel', 'seat', 'tyre'}
>>> car-cycle
{'music', 'wheel', 'gear'}
>>> cycle-car
{'cadence', 'pedal'}
>>> cycle^car
{'music', 'gear', 'wheel', 'pedal', 'cadence'}
>>> # performs symmetric difference, displays all elements present in cyle,car
>>> # but not in both, so excludes intersection or common elements.
>>> for i in car:
	for i not in cycle:
		
SyntaxError: invalid syntax
>>> for i in car:
	tup_set = (,)
	if i not in cycle:
		tup_set.append(i)
	print(tup_set)
	
SyntaxError: invalid syntax
>>> for i in car:
	tup_set = (,)
	if i not in cycle:
		tup_set.append(i)
	print(tup_set)
	
SyntaxError: invalid syntax
>>> for i in car:
	tup_set = []
	if i not in cycle:
		tup_set.append(i)
	print(tup_set)

	
['gear']
['music']
['wheel']
[]
[]
>>> tup_set = [];for i in car:
	if i not in cycle:
		tup_set.append(i)

	
SyntaxError: invalid syntax
>>> tup_set = []
>>> for i in car:
	if i not in cycle;
	
SyntaxError: invalid syntax
>>> for i in car:
	if i not in cycle:
		tup_set.append(i)

		
>>> print(tup_set)
['gear', 'music', 'wheel']
>>> print(set(tup_set))
{'music', 'wheel', 'gear'}
>>> set_intersection = []
>>> for i in car:
	if i in cycle;
	
SyntaxError: invalid syntax
>>> for i in car:
	if i in cycle:
		set_inter.append(i)

		
Traceback (most recent call last):
  File "<pyshell#49>", line 3, in <module>
    set_inter.append(i)
NameError: name 'set_inter' is not defined
>>> for i in car:
	if i in cycle:
		set_intersection.append(i)

		
>>> print(set(set_intersection))
{'seat', 'tyre'}
>>> set_union = []
>>> for i in  car or cycle:
	set_union.append(i)

	
>>> print(set(set_union))
{'gear', 'music', 'wheel', 'seat', 'tyre'}
>>> car or cycle
{'gear', 'music', 'wheel', 'seat', 'tyre'}
>>> car | cycle
{'gear', 'pedal', 'cadence', 'music', 'wheel', 'seat', 'tyre'}
>>> cycle or car
{'cadence', 'seat', 'pedal', 'tyre'}
>>> # when we use or operator, only the first set's elements are taken if not
>>>        # if not empty else the other will be.
>>> set_union = []
>>> for i in (car,cycle):
	set_union.append(i)

	
>>> print(set_union)
[{'gear', 'music', 'wheel', 'seat', 'tyre'}, {'cadence', 'seat', 'pedal', 'tyre'}]
>>> # appends {set
>>> # appends {set} car and cycle as elements for set_union list, nested
>>> set_union = []
>>> for i in car|cycle:
	set_union.append(i)

	
>>> print(set_union)
['gear', 'pedal', 'cadence', 'music', 'wheel', 'seat', 'tyre']
>>> set_union = []
>>> for i in cycle:
	if i in car:
		set_union.append(i)

		
>>> print(set(set_union))
{'seat', 'tyre'}
>>> set_symmetric_difference = []
>>> for i in cycle:
	if i in car:
		if i in car&cycle:
			continue
		set_symmetric_difference.append(i)

		
>>> print(set_symmetric_difference)
[]
>>> car and cycle
{'cadence', 'seat', 'pedal', 'tyre'}
>>> car & cycle
{'seat', 'tyre'}
>>> cycle and car
{'gear', 'music', 'wheel', 'seat', 'tyre'}
>>> #while using 'and' operator, the second one is displayed.
>>> set_symmetric_difference and cycle
[]
>>> set() and cycle
set()
>>> # empty set evaluates to false so same is returned as output
>>> print(set() and cycle)
set()
>>> if set() and cycle:
	print(true)
	break
SyntaxError: 'break' outside loop
>>> if set() and cycle:
	print(true)

	
>>> if car and cycle:
	print('true')

	
true
>>> if set() and cycle:
	print('true')

	
>>> for i in cycle:
	if i in car & cycle:
		continue
	else:
		set_symmetric_difference.append(i)

		
>>> print(set_symmetric_difference)
['cadence', 'pedal']
>>> for i in car:
	if i in car & cycle:
		continue
	else:
		set_symmetric_difference.append(i)

		
>>> print(set_symmetric_difference)
['cadence', 'pedal', 'gear', 'music', 'wheel']
>>> for i in car|cycle:
	if i in car & cycle:
		continue
	else:
		set_symmetric_difference.append(i)

		
>>> print(set_symmetric_difference)
['cadence', 'pedal', 'gear', 'music', 'wheel', 'gear', 'pedal', 'cadence', 'music', 'wheel']
>>> del set_symmetric_difference
>>> set_symmetric_difference = []
>>> for i in car|cycle:
	if i not in car & cycle:
	    set_symmetric_difference.append(i)

	    
>>> print(set_symmetric_difference)
['gear', 'pedal', 'cadence', 'music', 'wheel']
>>> car ^ cycle
{'gear', 'pedal', 'cadence', 'music', 'wheel'}
>>> """Firstly, just the elements of set- car were taken in for loop,
     intersection was eliminated, result displayed.
     Similar with the second case of for i in  cycle:
     Finally, we went with for i in car|cycle:(checked i in union of two sets)
     thereafter, excluded the intersection by testing the if condition,
     if i not in car&cycle:(membership operator 'not in'), thus the result."""
"Firstly, just the elements of set- car were taken in for loop,\n     intersection was eliminated, result displayed.\n     Similar with the second case of for i in  cycle:\n     Finally, we went with for i in car|cycle:(checked i in union of two sets)\n     thereafter, excluded the intersection by testing the if condition,\n     if i not in car&cycle:(membership operator 'not in'), thus the result."
>>> 
