Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Dog:
	kind = 'canine'
	# class variable, static field in Java
	# doesn't change with every instantiation of Dog class.
	def __init__(self, name):
		# constructor in Java
		self.name = name
		# instance variable, non-static field in Java
		# changes with every instantiation of Dog Class.

		
>>> d = Dog('Foggy')
>>> e = Dog() # expects one argument bcoz constructor expects positional arg
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    e = Dog() # expects one argument bcoz constructor expects positional arg
TypeError: __init__() missing 1 required positional argument: 'name'
>>> e = Dog('buddy')
>>> d.kind
'canine'
>>> e.kind
'canine'
>>> # for both the instance objects, d and e, class variables remain the same
>>> d.name
'Foggy'
>>> e.name
'buddy'
>>> # instance variables change with every new instance of Dog class,
>>> # depends upon the argument passed with every instantiation.
>>> class Dog:
	kind = []
	# class variable, static field in Java
	# doesn't change with every instantiation of Dog class.
	def __init__(self, name):
		# constructor in Java
		self.name = name
		# instance variable, non-static field in Java
		# changes with every instantiation of Dog Class.
	def add_kind(self, k):
		# first argument is always a Class Object
		kind.append(k)

		
>>> d = Dog('foggy')
>>> e = Dog('buddy')
>>> d.add_kind('canine')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d.add_kind('canine')
  File "<pyshell#24>", line 12, in add_kind
    kind.append(k)
NameError: name 'kind' is not defined
>>> class Dog:
	kind = []
	# class variable, static field in Java
	# doesn't change with every instantiation of Dog class.
	def __init__(self, name):
		# constructor in Java
		self.name = name
		# instance variable, non-static field in Java
		# changes with every instantiation of Dog Class.
	def add_kind(self, k):
		# first argument is always a Class Object
		self.kind.append(k)

		
>>> d.add_kind('canine')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d.add_kind('canine')
  File "<pyshell#24>", line 12, in add_kind
    kind.append(k)
NameError: name 'kind' is not defined
>>> d = Dog('foggy')
>>> e = Dog('buddy')
>>> d.add_kind('canine')
>>> e.add_kind('canibal')
>>> d.kind
['canine', 'canibal']
>>> e.kind
['canine', 'canibal']
>>> # In the first example, we mentioned kind.append(k), code looked for kind
>>> # as global variable outside class so threw NameError exception
>>> # In second one, we directly tried to access d.add_kind('canine')
>>> # without creating the object first so displayed error.
>>> # This exception raised because instance of class wasn't created and we
>>> # tried to instantiate class without an Instance object.
>>> # When using a mutable object as class variable we get same result for both
>>> # objects which we wouldn't have wanted.
>>> # It's possible bcoz class variables are available for all instances of clas
>>> # To remove this and restrict things to instance objects specifically,
>>> class Dog:
	kind = 'canine'
	# class variable, static field in Java
	# doesn't change with every instantiation of Dog class.
	def __init__(self, name, species):
		# constructor in Java
		self.name = name
		self.species = species
		# instance variable, non-static field in Java
		# changes with every instantiation of Dog Class.
	def add_kind(self, k):
		# first argument is always a Class Object
		self.species.append(k)

		
>>> d.name('rocket')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d.name('rocket')
TypeError: 'str' object is not callable
>>> e = Dog('buddy')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    e = Dog('buddy')
TypeError: __init__() missing 1 required positional argument: 'species'
>>> class Dog:
	kind = 'canine'
	# class variable, static field in Java
	# doesn't change with every instantiation of Dog class.
	def __init__(self, name):
		# constructor in Java
		self.name = name
		self.species = []
		# instance variable, non-static field in Java
		# changes with every instantiation of Dog Class.
	def add_kind(self, k):
		# first argument is always a Class Object
		self.species.append(k)

		
>>> e = Dog('buddy')
>>> d = Dog('foggy')
>>> d.add_kind('German Shephard')
>>> d.species
['German Shephard']
>>> e.add_kind("Bull Dog")
>>> d.species
['German Shephard']
>>> e.species
['Bull Dog']
>>> 
